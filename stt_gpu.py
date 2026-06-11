import os
import sys
import time
import argparse
import threading
import whisper
import torch  # GPU 사용을 위해 torch 추가

# 글로벌 실행 상태 변수
is_running = False

def show_progress():
    global is_running
    chars = ['|', '/', '-', '\\']
    idx = 0
    while is_running:
        # 실행 중임을 알리는 애니메이션 텍스트 출력
        sys.stdout.write(f'\r실행중~ 음성 파일 변환 진행 중입니다... {chars[idx % len(chars)]}')
        sys.stdout.flush()
        time.sleep(0.1)
        idx += 1

def main():
    global is_running
    
    # 프로그램 시작 시 파일 이름 매개변수 받기
    parser = argparse.ArgumentParser(description="Whisper STT 프로그램")
    parser.add_argument("filename", nargs="?", default="AI-W09-02-Simple Example 22 min.mp4", 
                        help="변환할 동영상/음성 파일 이름 (입력하지 않으면 기본 파일 사용)")
    parser.add_argument("--output-dir", help="전사 결과를 저장할 디렉토리")
    parser.add_argument("--output-name", help="저장할 txt 파일명 (예: 컴퓨터 구조 1-01-강의-목차.txt)")
    args = parser.parse_args()

    filename = args.filename

    if not os.path.exists(filename):
        print(f"오류: '{filename}' 파일을 찾을 수 없습니다. 경로와 파일명을 다시 확인해주세요.")
        sys.exit(1)

    # 전체 실행 시간 측정 시작
    start_time = time.time()

    # --- 추가된 부분: Mac GPU(MPS) 설정 ---
    if torch.backends.mps.is_available():
        device = "mps"
        print("[정보] Mac GPU(MPS) 가속을 사용합니다.")
    elif torch.cuda.is_available():
        device = "cuda"
        print("[정보] NVIDIA GPU(CUDA) 가속을 사용합니다.")
    else:
        device = "cpu"
        print("[정보] 사용할 수 있는 GPU가 없어 CPU 모드로 실행합니다.")
    # ------------------------------------

    # 1. 모델 로드 (device 파라미터 적용)
    print("1. 모델 로드 중...")
    model = whisper.load_model("turbo", device=device) 

    print(f"\n2. 파일 변환 시작: {filename}")
    
    # 진행상황 표시 스레드 시작
    is_running = True
    progress_thread = threading.Thread(target=show_progress)
    progress_thread.start()

    try:
        # 2. 음성 파일 변환 (한국어 지정으로 정확도/속도 향상)
        result = model.transcribe(filename, language="ko")
    finally:
        # 변환 완료 후 스레드 종료
        is_running = False
        progress_thread.join()
        sys.stdout.write('\r음성 파일 변환 완료!                                     \n')

    # 3. 변환된 텍스트 출력
    print("\n--- 변환된 텍스트 ---")
    print(result["text"])
    print("---------------------\n")

    # 4. 파일명 중복 예외 처리 후 저장
    # 기본 저장 파일명 설정
    if args.output_dir:
        os.makedirs(args.output_dir, exist_ok=True)
        output_name = args.output_name or f"{os.path.splitext(os.path.basename(filename))[0]}.txt"
        output_filename = os.path.join(args.output_dir, output_name)
    else:
        base_video_name = os.path.splitext(filename)[0] # 확장자 제거
        output_filename = f"{base_video_name}.txt"

    # 파일명과 확장자(.txt) 분리
    base, ext = os.path.splitext(output_filename)

    counter = 1
    # 동일한 이름의 파일이 이미 존재한다면 반복문 실행
    while os.path.exists(output_filename):
        output_filename = f"{base}-{counter}{ext}"
        counter += 1

    # 최종 결정된 파일명으로 저장
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"전사 완료! 파일이 저장되었습니다: {output_filename}")

    # 전체 실행 시간 측정 종료 및 출력
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\n[!] 프로그램 총 실행 시간: {elapsed_time:.2f}초")

if __name__ == "__main__":
    main()
