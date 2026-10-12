# TODO: 평가 피드백·로그 분석 — 아래 실행 가능한 코드를 수정하여 결과를 비교하세요.
# 교재 최신 API·State 구조와 일치하는 실습 시작 파일입니다.

from datetime import datetime

def trace(step: str, detail: str) -> None:
    # 실행 시각과 현재 단계를 한 줄의 로그로 남깁니다.
    timestamp = datetime.now().isoformat(timespec="seconds")
    print(f"[{timestamp}] {step:<12} {detail}")

trace("START", "사용자 요청 수신")
trace("TOOL", "상품 정보 조회")
trace("OBSERVATION", "재고 0개")
trace("GATE", "품절 안내 경로 선택")
trace("END", "응답 완료")
