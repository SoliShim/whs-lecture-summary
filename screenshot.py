#!/usr/bin/env python3
"""
Extract screenshots from one video, or from every supported video in a directory,
at a fixed interval using FFmpeg.

Example:
    python3 extract_screenshots.py "/path/to/movie.mp4"
    python3 extract_screenshots.py "/path/to/movie.mp4" 15
    python3 extract_screenshots.py "/path/to/video-folder"
    python3 extract_screenshots.py "/path/to/video-folder" 10 --recursive
    python3 extract_screenshots.py "/path/to/movie.mp4" --interval 15 --format jpg
    python3 extract_screenshots.py "/path/to/movie.mp4" --hwaccel auto
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


VIDEO_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".m4v",
    ".mkv",
    ".avi",
    ".webm",
    ".ts",
    ".mts",
    ".m2ts",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Extract screenshots from one video, or from every supported video "
            "in a directory. Each video gets its own output folder."
        )
    )
    parser.add_argument("source", help="Path to a source video file or directory.")
    parser.add_argument(
        "interval_seconds",
        nargs="?",
        type=float,
        help="Screenshot interval in seconds. Default: 15",
    )
    parser.add_argument(
        "--interval",
        dest="interval_option",
        type=float,
        default=None,
        help="Screenshot interval in seconds. Default: 15",
    )
    parser.add_argument(
        "--format",
        choices=("jpg", "png"),
        default="jpg",
        help="Output image format. Default: jpg",
    )
    parser.add_argument(
        "--output-root",
        help=(
            "Directory where the result folder will be created. "
            "Default: the same directory as each source video."
        ),
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing screenshot files in the output folder.",
    )
    parser.add_argument(
        "--hwaccel",
        choices=("auto", "videotoolbox", "off"),
        default="auto",
        help=(
            "Hardware decoding mode. On macOS, auto tries Apple VideoToolbox first "
            "and falls back to CPU if it fails. Default: auto"
        ),
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="When the source is a directory, also scan subdirectories.",
    )
    return parser.parse_args()


def get_interval(args: argparse.Namespace) -> float:
    interval = (
        args.interval_option
        if args.interval_option is not None
        else args.interval_seconds
        if args.interval_seconds is not None
        else 15
    )

    if interval <= 0:
        print("간격 값은 0보다 커야 합니다.", file=sys.stderr)
        raise SystemExit(1)

    return interval


def require_ffmpeg() -> None:
    if shutil.which("ffmpeg") is None:
        print(
            "ffmpeg를 찾을 수 없습니다. macOS에서는 보통 `brew install ffmpeg`로 설치합니다.",
            file=sys.stderr,
        )
        raise SystemExit(1)


def ffmpeg_supports_videotoolbox() -> bool:
    completed = subprocess.run(
        ["ffmpeg", "-hide_banner", "-hwaccels"],
        check=False,
        text=True,
        capture_output=True,
    )
    return completed.returncode == 0 and "videotoolbox" in completed.stdout.lower()


def make_output_pattern(
    video_path: Path,
    output_root: Path | None,
    image_format: str,
) -> tuple[Path, Path]:
    video_stem = video_path.stem
    root = output_root if output_root else video_path.parent
    output_dir = root / video_stem
    output_dir.mkdir(parents=True, exist_ok=True)

    # FFmpeg expands %04d into 0001, 0002, ...
    output_pattern = output_dir / f"{video_stem} - %04d.{image_format}"
    return output_dir, output_pattern


def is_supported_video(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in VIDEO_EXTENSIONS


def collect_video_paths(source_path: Path, recursive: bool) -> list[Path]:
    if source_path.is_file():
        return [source_path]

    if not source_path.is_dir():
        print(f"입력 경로를 찾을 수 없습니다: {source_path}", file=sys.stderr)
        raise SystemExit(1)

    iterator = source_path.rglob("*") if recursive else source_path.iterdir()
    return sorted(path for path in iterator if is_supported_video(path))


def run_ffmpeg(
    video_path: Path,
    output_pattern: Path,
    interval: float,
    image_format: str,
    overwrite: bool,
    use_videotoolbox: bool,
) -> None:
    fps_value = f"1/{interval:g}"
    command = [
        "ffmpeg",
        "-hide_banner",
        "-nostdin",
    ]

    if use_videotoolbox:
        command += [
            "-hwaccel",
            "videotoolbox",
        ]

    command += [
        "-i",
        str(video_path),
        "-vf",
        f"fps={fps_value}",
    ]

    if image_format == "jpg":
        command += ["-q:v", "2"]

    command += ["-start_number", "1"]
    command += ["-y" if overwrite else "-n"]
    command += [str(output_pattern)]

    print("실행 중:", " ".join(command))
    completed = subprocess.run(command, check=False)
    if completed.returncode != 0:
        raise subprocess.CalledProcessError(completed.returncode, command)


def should_try_videotoolbox(hwaccel: str) -> bool:
    if hwaccel == "off":
        return False

    if hwaccel == "videotoolbox":
        return True

    return sys.platform == "darwin" and ffmpeg_supports_videotoolbox()


def extract_screenshots(
    video_path: Path,
    output_root: Path | None,
    interval: float,
    image_format: str,
    overwrite: bool,
    hwaccel: str,
    use_videotoolbox: bool,
) -> Path:
    output_dir, output_pattern = make_output_pattern(
        video_path=video_path,
        output_root=output_root,
        image_format=image_format,
    )

    print(f"\n처리 중: {video_path}")

    try:
        run_ffmpeg(
            video_path=video_path,
            output_pattern=output_pattern,
            interval=interval,
            image_format=image_format,
            overwrite=overwrite,
            use_videotoolbox=use_videotoolbox,
        )
    except subprocess.CalledProcessError as error:
        if use_videotoolbox and hwaccel == "auto":
            print("VideoToolbox 처리에 실패해서 CPU 방식으로 다시 시도합니다.")
            try:
                run_ffmpeg(
                    video_path=video_path,
                    output_pattern=output_pattern,
                    interval=interval,
                    image_format=image_format,
                    overwrite=overwrite,
                    use_videotoolbox=False,
                )
            except subprocess.CalledProcessError as retry_error:
                raise subprocess.CalledProcessError(
                    retry_error.returncode,
                    retry_error.cmd,
                ) from retry_error
        else:
            raise subprocess.CalledProcessError(error.returncode, error.cmd) from error

    print(f"완료: {output_dir}")
    return output_dir


def main() -> None:
    args = parse_args()
    require_ffmpeg()

    source_path = Path(args.source).expanduser().resolve()

    interval = get_interval(args)
    output_root = Path(args.output_root).expanduser().resolve() if args.output_root else None
    video_paths = collect_video_paths(source_path, args.recursive)
    if not video_paths:
        print(f"처리 가능한 동영상 파일이 없습니다: {source_path}", file=sys.stderr)
        raise SystemExit(1)

    if source_path.is_file() and not is_supported_video(source_path):
        print(
            f"지원 목록에 없는 확장자입니다: {source_path.suffix or '(확장자 없음)'}",
            file=sys.stderr,
        )
        raise SystemExit(1)

    print(f"처리할 동영상 수: {len(video_paths)}")
    use_videotoolbox = should_try_videotoolbox(args.hwaccel)
    failed_paths: list[Path] = []

    for video_path in video_paths:
        try:
            extract_screenshots(
                video_path=video_path,
                output_root=output_root,
                interval=interval,
                image_format=args.format,
                overwrite=args.overwrite,
                hwaccel=args.hwaccel,
                use_videotoolbox=use_videotoolbox,
            )
        except subprocess.CalledProcessError:
            failed_paths.append(video_path)
            print(f"실패: {video_path}", file=sys.stderr)

    if failed_paths:
        print("\n실패한 파일:", file=sys.stderr)
        for failed_path in failed_paths:
            print(f"- {failed_path}", file=sys.stderr)
        raise SystemExit(1)

    print("\n전체 완료")


if __name__ == "__main__":
    main()
