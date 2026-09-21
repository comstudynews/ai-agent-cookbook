from datetime import datetime

def trace(step: str, detail: str) -> None:
    # 실행 시각과 현재 단계를 한 줄의 로그로 남깁니다.
    timestamp = datetime.now().isoformat(timespec="seconds")
    # TODO: 한 줄 Trace 로그를 출력하세요.
    ...

trace("START", "사용자 요청 수신")
trace("TOOL", "상품 정보 조회")
trace("OBSERVATION", "재고 0개")
trace("GATE", "품절 안내 경로 선택")
trace("END", "응답 완료")
