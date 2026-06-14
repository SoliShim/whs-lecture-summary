import os
import sys
import time
import argparse
import threading
import whisper
import torch  # GPU 사용을 위해 torch 추가

# 글로벌 실행 상태 변수
is_running = False
current_index = 0
total_files = 0
current_filename = ""

# 디렉토리를 입력받았을 때 미디어 파일만 고르기 위한 확장자 목록
# 실제 변환 로직은 기존처럼 whisper.transcribe()에 그대로 맡깁니다.
MEDIA_EXTENSIONS = {
    # audio
    ".3ga", ".8svx", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape", ".au",
    ".dss", ".dsf", ".flac", ".m4a", ".m4b", ".m4p", ".mp3", ".mpga", ".oga",
    ".ogg", ".opus", ".qcp", ".tta", ".voc", ".wav", ".wma", ".wv",
    # video
    ".3g2", ".3gp", ".asf", ".avi", ".divx", ".dv", ".f4v", ".flv", ".m2ts", ".m4v",
    ".mkv", ".mod", ".mov", ".mp4", ".mpe", ".mpeg", ".mpg", ".mts", ".mxf", ".ogv",
    ".rm", ".rmvb", ".ts", ".vob", ".webm", ".wmv",
}


def is_media_file(filename):
    return os.path.splitext(filename)[1].lower() in MEDIA_EXTENSIONS


def get_media_files(path):
    # 파일 하나를 입력한 경우: 기존 코드처럼 그 파일 하나만 처리
    if os.path.isfile(path):
        return [path]

    # 디렉토리를 입력한 경우: 디렉토리 안의 미디어 파일들을 모두 수집
    if os.path.isdir(path):
        media_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                if is_media_file(full_path):
                    media_files.append(full_path)
        return sorted(media_files)

    print(f"오류: '{path}' 파일 또는 디렉토리를 찾을 수 없습니다. 경로와 이름을 다시 확인해주세요.")
    sys.exit(1)


def show_progress():
    global is_running
    chars = ['|', '/', '-', '\\']
    idx = 0
    while is_running:
        # 실행 중임을 알리는 애니메이션 텍스트 출력
        sys.stdout.write(
            f'\r[{current_index}/{total_files}] 실행중~ 음성 파일 변환 진행 중입니다... {chars[idx % len(chars)]}'
        )
        sys.stdout.flush()
        time.sleep(0.1)
        idx += 1


def main():
    global is_running, current_index, total_files, current_filename

    # 프로그램 시작 시 파일 이름 또는 디렉토리 이름 매개변수 받기
    parser = argparse.ArgumentParser(description="Whisper STT 프로그램")
    parser.add_argument("filename", nargs="?", default="AI-W09-02-Simple Example 22 min.mp4",
                        help="변환할 동영상/음성 파일 이름 또는 미디어 파일들이 들어있는 디렉토리 이름")
    parser.add_argument("--output-dir", help="전사 결과를 저장할 디렉토리")
    parser.add_argument("--prefix", help="순번 파일명 접두어. 지정하지 않으면 입력 영상 파일명을 그대로 사용합니다.")
    parser.add_argument("--start-index", type=int, default=1, help="첫 번째 출력 파일 번호 (기본값: 1)")
    args = parser.parse_args()

    input_path = args.filename
    media_files = get_media_files(input_path)

    if len(media_files) == 0:
        print(f"오류: '{input_path}' 디렉토리 안에서 변환할 미디어 파일을 찾을 수 없습니다.")
        sys.exit(1)

    total_files = len(media_files)
    print(f"[정보] 변환할 미디어 파일 수: {total_files}개")

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

    for index, filename in enumerate(media_files, start=1):
        current_index = index
        current_filename = filename

        print(f"\n2. 파일 변환 시작 ({index}/{total_files}): {filename}")

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
            if args.prefix:
                lesson_no = args.start_index + index - 1
                output_name = f"{args.prefix}-{lesson_no:02d}.txt"
            else:
                output_name = f"{os.path.splitext(os.path.basename(filename))[0]}.txt"
            output_filename = os.path.join(args.output_dir, output_name)
        else:
            base_video_name = os.path.splitext(filename)[0]  # 확장자 제거
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
        print(f"[전체 진행률] {index}/{total_files}개 완료 ({index / total_files * 100:.1f}%)")

    # 전체 실행 시간 측정 종료 및 출력
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\n[!] 프로그램 총 실행 시간: {elapsed_time:.2f}초")


if __name__ == "__main__":
    main()
