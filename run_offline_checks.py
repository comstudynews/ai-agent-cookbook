"""OpenAI API 호출 없이 실행할 수 있는 주요 LangGraph 실습을 검사합니다."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CASES = {
    "step05_graph.py": "HELLO AGENT",
    "step06_loop.py": "최종 시도 횟수: 3",
    "step07_workflow.py": "재시도 횟수: 1",
    "step08_agentic_rag_loop.py": "배송은",
    "step09_handoff.py": "기술 문의 처리 완료",
    "step11_parallel.py": "Fan-in 확인",
    "step11_no_reducer.py": "예상 오류: InvalidUpdateError",
    "step12_retry.py": "외부 API 호출 성공",
    "step13_hitl.py": "거절됨(미실행)",
    "extra_messages.py": "수정된 질문",
    "extra_messages_state.py": "입력 확인:",
    "extra_checkpointer.py": "메시지 수:",
}

def main():
    failures = 0
    for filename, expected in CASES.items():
        r = subprocess.run([sys.executable, str(ROOT / filename)], cwd=ROOT,
                           capture_output=True, text=True, timeout=90)
        ok = r.returncode == 0 and expected in r.stdout
        print(f"{'PASS' if ok else 'FAIL'}: {filename}")
        if not ok:
            failures += 1
            print(r.stdout[-700:], r.stderr[-1000:])
    print(f"오프라인 검사: {len(CASES)-failures}/{len(CASES)}")
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
