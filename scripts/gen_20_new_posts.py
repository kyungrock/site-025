#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""고양이 마사지 신규 20편 — 카테고리 중복 없음, 2026-07-09"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_PATH = ROOT / "data" / "blog-posts.json"
TODAY = "2026-07-09"


def tip(t: str) -> str:
    return f'<div class="tip-box">\n<strong>팁</strong>\n{t}\n</div>'


def warn(t: str) -> str:
    return f'<div class="warn-box">\n<strong>주의</strong>\n{t}\n</div>'


def related(*links: tuple[str, str]) -> str:
    items = "".join(f'<li><a href="blog/{hid}.html">{title}</a></li>' for hid, title in links)
    return f"<h2>함께 읽으면 좋은 글</h2>\n<ul>{items}</ul>"


NEW_POSTS = [
    {
        "id": "wfh-desk-cat-massage-break",
        "category": "재택·텔레워크",
        "emoji": "💻",
        "title": "재택근무 중 5분 고양이 마사지 — 책상 옆에서 쉬는 법",
        "summary": "화상회의 사이, 점심 직후, 퇴근 전. 재택 집사가 책상 옆 고양이와 5분 이완 루틴을 만드는 실전 가이드.",
        "tags": ["재택근무", "텔레워크", "고양이마사지", "휴식"],
        "content": """
<p class="article-lead">재택근무를 하다 보면 <strong>고양이는 발밑에, 나는 모니터에</strong> 고정되는 날이 많습니다. 저도 처음엔 「일 중엔 건드리지 말자」고 생각했는데, 오히려 5분 터치를 넣은 뒤로 집중이 더 잘 되더군요.</p>
<h2>왜 재택에서 마사지가 맞을까</h2>
<p>사무실과 달리 집에서는 고양이가 <strong>내 리듬을 온종일 지켜봅니다</strong>. 스트레스를 받으면 그걸 먼저 아는 경우가 많아요. 짧은 스트로킹은 고양이에게는 관심·안정 신호, 집사에게는 눈과 손을 쉬게 하는 <strong>마이크로 브레이크</strong>가 됩니다.</p>
<p>마사지·힐링·웰니스를 같이 챙기는 20~50대 집사에게, 재택 환경은 오히려 「매일 같은 장소·같은 시간」 루틴을 만들기 좋습니다.</p>
<h2>5분 루틴 — 회의 전·후 추천</h2>
<ol>
<li><strong>1분</strong> — 자리에서 일어나 창문·환기만 30초. 고양이가 따라오면 볼·턱만 가볍게.</li>
<li><strong>2분</strong> — 바닥 매트나 소파에 앉아 목 뒤→등 중앙 스트로킹. 손목·어깨도 함께 내립니다.</li>
<li><strong>1분</strong> — 고양이가 싫어하면 여기서 종료. 꼬리 휘둘림·귀 뒤로 젖힘 시 즉시 멈춤.</li>
<li><strong>1분</strong> — 물 한 잔, 다시 책상. 「돌아왔다」는 짧은 말로 마무리.</li>
</ol>
<h2>재택 집사가 자주 하는 실수</h2>
<ul>
<li>키보드 위·모니터 앞에서 억지로 끌어안기</li>
<li>마감 직전 피곤한 상태에서 급하게 깊게 누르기</li>
<li>회의 중 고양이 발소리·골골송을 「방해」로만 보기</li>
</ul>
<p>고양이 마사지는 <strong>일과의 끼워 넣기</strong>가 핵심입니다. 30분마다 알람을 맞추기보다, 「화상 종료」「점심 후」「저녁 램프 켤 때」처럼 <em>이미 있는 이벤트</em>에 붙이면 오래 갑니다.</p>
""" + tip("노트북 옆에 작은 브러시를 두면, 마사지 전 털 한 번 정리하기 좋습니다.") + warn("웰니스·생활 정보이며 수의 진료를 대체하지 않습니다.") + related(
            ("evening-cat-massage-routine", "저녁 고양이 마사지 10분 루틴"),
            ("owner-relaxation-with-cat", "집사도 함께 이완하는 마사지"),
        ) + "<p>이 글은 <strong>재택·텔레워크</strong> 관점에서 고양이 마사지를 다룬 정보성 콘텐츠입니다.</p>",
    },
    {
        "id": "commute-stress-cat-welcome-massage",
        "category": "출퇴근·환영",
        "emoji": "🚇",
        "title": "퇴근 후 고양이 마사지 — 출근 스트레스를 집에서 내려놓기",
        "summary": "문 열자마자 달려오는 고양이, 그 10분이 하루를 바꿉니다. 출퇴근 집사를 위한 환영·이완 터치 가이드.",
        "tags": ["출퇴근", "퇴근", "스트레스", "환영"],
        "content": """
<p class="article-lead">현관문을 열면 <strong>먼저 오는 건 신발이 아니라 고양이</strong>인 집이 많습니다. 퇴근 후 10분, 그 순간을 마사지로 바꾸면 「회사 모드」에서 「집 모드」로 넘어가는 속도가 달라집니다.</p>
<h2>퇴근 직후 3분 — 순서가 중요합니다</h2>
<p>외출복·가방·핸드폰 알림을 잠깐 내려놓은 뒤 손을 씻고 시작하세요. 고양이 코에는 <strong>낯선 냄새</strong>가 먼저 전달됩니다. 손등으로 냄새 맞추기 → 볼·턱 30초 → 목 뒤 1분 → 등 1분 30초.</p>
<h2>출근 전 2분 — 아침에도 짧게</h2>
<p>아침은 시간이 촉박하지만, <strong>밥그릇 옆에서 2분</strong>만 해도 「오늘도 돌아온다」는 신호가 됩니다. 아침 루틴 글과 겹치지 않게, 여기서는 <em>출근·퇴근 전환</em>에 초점을 둡니다.</p>
<h2>지하철·운전 피로와 연결하기</h2>
<p>집사 어깨가 굳어 있으면 손 힘이 무거워집니다. 퇴근 후 <strong>어깨를 세 번 내린 다음</strong> 고양이를 만지면, 무의식적으로 누르는 힘이 줄어듭니다. 고양이 마사지는 반려묘만을 위한 게 아니라, 집사의 호흡·긴장을 풀는 셀프케어와 한 세트입니다.</p>
""" + tip("퇴근 후 바로 목욕·샤워하는 날은, 샤워 전 1분만 해도 충분합니다.") + related(
            ("morning-cat-massage-routine", "아침 3분 마사지"),
            ("stress-relief-cat-massage", "스트레스 받은 고양이 진정 루틴"),
        ) + "<p>이 글은 <strong>출퇴근·환영</strong> 관점의 고양이 마사지 정보입니다.</p>",
    },
    {
        "id": "hand-warmth-touch-cat",
        "category": "체온·손끝",
        "emoji": "🤲",
        "title": "손 차가우면 고양이가 피한다 — 체온·손끝 준비법",
        "summary": "차가운 손, 건조한 손, 향기 강한 로션. 고양이가 마사지를 싫어하는 이유 중 하나는 ‘손’일 수 있습니다.",
        "tags": ["체온", "손끝", "터치", "준비"],
        "content": """
<p class="article-lead">「만지면 도망간다」고 하시는 분 중 상당수는 <strong>기술 문제가 아니라 손 문제</strong>인 경우가 있습니다. 고양이 피부는 우리보다 민감하고, 특히 겨울·에어컨 아래에서는 손 차가움이 크게 느껴집니다.</p>
<h2>손을 ‘만져도 되는 온도’로</h2>
<ul>
<li>30초간 손바닥을 문지르거나 온수에 담그기</li>
<li>향 없는·저자극 보습제 (양은 아주 적게)</li>
<li>손톱·스킨·거친 각질 정리</li>
</ul>
<h2>여름과 겨울 차이</h2>
<p>여름엔 <strong>땀·끈적임</strong>이, 겨울엔 <strong>정전기·건조</strong>가 원인입니다. 여름엔 손을 가볍게 씻고, 겨울엔 가습과 손 보습을 마사지 전 루틴에 넣어 보세요.</p>
<h2>고양이 반응으로 확인</h2>
<p>손을 내밀었을 때 코를 대고 냄새를 맡은 뒤 <strong>머리를 비비면 OK</strong>, 몸을 돌리면 그날은 1분만·볼만 터치하세요.</p>
""" + tip("마사지 전에 손등을 고양이 코에 3초 대면, 서로 냄새를 맞추는 시간이 됩니다.") + related(
            ("pre-massage-preparation", "마사지 전 준비"),
            ("winter-dry-skin-massage", "겨울 건조기 시즌 마사지"),
        ) + "<p>이 글은 <strong>체온·손끝</strong> 관점의 터치 준비 정보입니다.</p>",
    },
    {
        "id": "shoulder-tension-owner-cat-dual-relax",
        "category": "어깨·긴장",
        "emoji": "😮‍💨",
        "title": "어깨가 뭉친 날 — 집사와 고양이 같이 푸는 7분",
        "summary": "집사 어깨 긴장이 손에 전달됩니다. 어깨·목·등을 연결한 7분 듀얼 이완 루틴.",
        "tags": ["어깨", "긴장", "이완", "듀얼"],
        "content": """
<p class="article-lead">하루 종일 모니터를 본 날, 손가락만 고양이에게 가고 <strong>어깨 힘은 그대로</strong>인 적 없으신가요? 고양이는 그 ‘무거운 손’을 금방 압니다.</p>
<h2>7분 구성</h2>
<ol>
<li>집사: 어깨 으쓱 3회 → 내리기 3회 (1분)</li>
<li>고양이: 볼·목 뒤 스트로킹 (2분)</li>
<li>집사: 깊은 호흡 4회, 배·갈비뼈 옆 이완 (1분)</li>
<li>고양이: 등 양옆 근육 따라 천천히 (3분)</li>
</ol>
<h2>왜 어깨부터인가</h2>
<p>긴장된 승모근·어깨는 손목·손가락 힘으로 이어집니다. 마사지·힐링·웰니스에서 말하는 「이완」은 고양이만 풀어주는 게 아니라, <strong>집사 몸의 출발점</strong>을 바꾸는 일이기도 합니다.</p>
""" + warn("고양이 목·척추에 강한 압을 가하지 마세요.") + related(
            ("neck-shoulder-cat-massage", "목·어깨 5분 루틴"),
            ("owner-relaxation-with-cat", "집사 이완 연계"),
        ) + "<p>이 글은 <strong>어깨·긴장</strong> 관점의 듀얼 이완 가이드입니다.</p>",
    },
    {
        "id": "breathing-sync-cat-massage",
        "category": "호흡·동기화",
        "emoji": "🌬️",
        "title": "호흡 맞추며 고양이 마사지 — 4-6 리듬 쓰다듬기",
        "summary": "들이쉬며 손을 올리고, 내쉬며 쓸어내리기. 호흡과 스트로킹을 맞추면 터치가 부드러워집니다.",
        "tags": ["호흡", "리듬", "이완", "마사지"],
        "content": """
<p class="article-lead">「천천히 하라」는 말은 쉽지만, 손만 느리게 하다 보면 어색해질 때가 있습니다. <strong>호흡을 메트로놈</strong>처럼 쓰면 리듬이 자연스럽게 맞습니다.</p>
<h2>4-6 패턴 따라하기</h2>
<p>코로 4초 들이쉬며 손을 고양이 등에 올리고, 6초 내쉬며 아래로 쓸어내립니다. 5회 반복 후 30초 쉬기. 고양이가 골골송을 시작하면 속도를 유지하세요.</p>
<h2>마사지·웰니스와의 연결</h2>
<p>사람 마사지 전후에 호흡을 쓰는 것처럼, 고양이 터치에도 같은 원리가 통합니다. 긴장이 높은 날·새로 입양한 날·병원 다녀온 다음 날 특히 도움이 됩니다.</p>
<h2>실패하기 쉬운 점</h2>
<ul>
<li>호흡만 신경 쓰다 손가락 끝으로 찌르기</li>
<li>고양이가 일어나려 할 때 억지로 계속하기</li>
</ul>
""" + tip("눈을 감고 해도 됩니다. 시각 정보를 줄이면 손 감각에 집중하기 쉽습니다.") + related(
            ("stress-relief-cat-massage", "스트레스 완화 마사지"),
            ("bedtime-massage-cat", "잠들기 전 마사지"),
        ) + "<p>이 글은 <strong>호흡·동기화</strong> 관점의 터치 리듬 가이드입니다.</p>",
    },
    {
        "id": "arthritis-senior-cat-joint-massage",
        "category": "관절·시니어",
        "emoji": "🦴",
        "title": "관절이 뻣뻣한 노묘 — 마사지로 ‘움직임’ 돕기",
        "summary": "노령고양이 관절·허리·골반 주변. 직접 관절을 꾹 누르지 않고, 주변 근육을 풀어주는 접근.",
        "tags": ["관절", "노묘", "시니어", "케어"],
        "content": """
<p class="article-lead">10살, 12살, 15살—나이가 들수록 <strong>점프·높이 올라가기</strong>가 줄어드는 고양이가 많습니다. 노령고양이 글과 겹치지 않게, 여기서는 <em>관절 주변 근육</em>에 초점을 둡니다.</p>
<h2>하지 말 것</h2>
<ul>
<li>관절을 꾹 누르거나 ‘뚜둑’ 소리 나게 비틀기</li>
<li>아픈 다리를 억지로 펴기</li>
<li>30분 이상 같은 자세 유지시키기</li>
</ul>
<h2>해도 되는 것</h2>
<p>누운 자세에서 <strong>등·옆구리·어깨 윗부분</strong>을 3~5분 가볍게. 따뜻한 담요 위, 방 온도 22~24°C 정도. 통증 의심 시 수의사와 상담 후 시작하세요.</p>
<h2>집사가 기록하면 좋은 것</h2>
<p>「어느 쪽 다리를 덜 올림」「어느 날 싫어함」을 메모하면, 마사지가 아니라 <strong>건강 체크</strong> 도구가 되기도 합니다.</p>
""" + warn("절뚝거림·식욕 감소·화장실 습관 변화는 마사지보다 진료가 우선입니다.") + related(
            ("senior-cat-gentle-massage", "노령고양이 부드러운 마사지"),
            ("pain-signals-stop-massage", "중단 신호"),
        ) + "<p>이 글은 <strong>관절·시니어</strong> 관점의 케어 정보입니다.</p>",
    },
    {
        "id": "humidity-indoor-cat-skin-massage",
        "category": "습도·실내",
        "emoji": "💧",
        "title": "습도 40% 이하일 때 — 실내 건조와 고양이 피부·털 마사지",
        "summary": "가습·브러시·손 마사지를 묶는 실내 케어. 겨울 건조 글과 다른 ‘습도 숫자’ 중심 가이드.",
        "tags": ["습도", "실내", "피부", "건조"],
        "content": """
<p class="article-lead">겨울 난방·여름 에어컨 아래 실내 습도는 <strong>40% 아래</strong>로 떨어지기 쉽습니다. 털이 푸석해지고, 정전기가 나면 고양이가 터치를 피하기도 합니다.</p>
<h2>습도 → 털 → 마사지 순서</h2>
<ol>
<li>가습기·습도계로 45~55% 목표 (과습도 곰팡이 주의)</li>
<li>핀 브러시로 표면 털 정리 2분</li>
<li>손바닥 전체로 등·옆구리 스트로킹 5분</li>
</ol>
<h2>정전기 줄이기</h2>
<p>금속 접지된 가습기, 면 담요, 손 보습을 병행하세요. 「뻣뻣한 털」은 마사지 한 번으로 해결되지 않을 때가 많습니다. <strong>환경 + 그루밍 + 터치</strong>가 세트입니다.</p>
""" + tip("마사지 전에 손에 물기를 살짝 묻히고 두드리면 정전기가 줄어드는 경우가 있습니다.") + related(
            ("winter-dry-skin-massage", "겨울 건조 시즌"),
            ("brush-massage-combo", "브러시+마사지"),
        ) + "<p>이 글은 <strong>습도·실내</strong> 환경과 터치를 연결한 가이드입니다.</p>",
    },
    {
        "id": "shedding-season-massage-brush",
        "category": "털갈이·계절",
        "emoji": "🍂",
        "title": "털갈이철 마사지 — 빗·손·휴식을 번갈아",
        "summary": "봄·가을 털갈이. 과한 빗질 후 손 마사지로 피부 진정시키는 루틴.",
        "tags": ["털갈이", "계절", "브러시", "그루밍"],
        "content": """
<p class="article-lead">털갈이철엔 소파·옷·밥그릇 옆에 <strong>털이 쌓입니다</strong>. 이때 빗질만 길게 하면 피부가 예민해져, 오히려 만지기를 싫어하는 고양이가 늘기도 합니다.</p>
<h2>15분 번갈아 루틴</h2>
<p><strong>3분 빗질 → 2분 손 스트로킹 → 1분 휴식</strong>을 3세트. 빗질은 한 방향, 배·다리 안쪽은 짧게. 손 마사지는 「빗질 끝 진정」 역할에 가깝습니다.</p>
<h2>장모·단모 차이</h2>
<p>장모는 엉킴 방지가 먼저, 단모는 피부 마사지·혈행 느낌이 더 와닿는 경우가 많습니다. 품종별 글과 함께 읽으면 좋습니다.</p>
""" + related(
            ("longhair-cat-massage", "장모종"),
            ("shorthair-cat-massage", "단모종"),
        ) + "<p>이 글은 <strong>털갈이·계절</strong> 관점의 그루밍+마사지입니다.</p>",
    },
    {
        "id": "eye-area-gentle-cat-touch",
        "category": "눈·주변",
        "emoji": "👁️",
        "title": "눈·눈꼬리 주변 — 건드려도 되는 선과 안 되는 선",
        "summary": "눈꼬리·눈두덩·이마. 눈물 자국·깜빡임을 보며 가볍게 터치하는 법.",
        "tags": ["눈", "눈꼬리", "터치", "안전"],
        "content": """
<p class="article-lead">눈은 고양이가 <strong>가장 조심하는 부위</strong> 중 하나입니다. 「눈 주변만 특별히」 다루는 방법을 알면, 전체 마사지 전 신뢰 테스트로도 쓸 수 있습니다.</p>
<h2>가능한 터치</h2>
<ul>
<li>이마에서 눈썹 방향으로 부드럽게 (눈알 건드리지 않음)</li>
<li>눈꼬리 바깥 1cm 부근, 손가락 끝이 아닌 손바닥 가장자리</li>
</ul>
<h2>피할 것</h2>
<ul>
<li>눈알·속눈썹 직접 접촉</li>
<li>눈곱을 억지로 떼기 (전용 패드·수의사 상담)</li>
</ul>
<p>눈을 꼭 감거나 고개를 돌리면 그날은 이마·볼만 하세요.</p>
""" + warn("눈 붉음·분비물 증가·눈을 안 뜸 → 마사지 중단, 진료.") + related(
            ("forbidden-zones-cat", "금지 부위"),
            ("cat-body-language-massage", "신호 읽기"),
        ) + "<p>이 글은 <strong>눈·주변</strong> 터치 안전 가이드입니다.</p>",
    },
    {
        "id": "scent-memory-cat-massage-blanket",
        "category": "냄새·담요",
        "emoji": "🧣",
        "title": "담요·쿠션에 남는 냄새 — 고양이가 좋아하는 ‘자리’ 만들기",
        "summary": "마사지+냄새 글과 다른, 담요·쿠션에 집사·고양이 냄새를 쌓는 환경 만들기.",
        "tags": ["냄새", "담요", "환경", "안정"],
        "content": """
<p class="article-lead">같은 손이라도 <strong>‘익숙한 담요 위’</strong>와 낯선 바닥은 반응이 다릅니다. 고양이는 후각으로 안전을 판단합니다.</p>
<h2>마사지 전용 자리 만들기</h2>
<ol>
<li>집사·고양이가 함께 쓰는 얇은 담요를 하나 정함</li>
<li>매일 비슷한 시간, 같은 자리에서 5분 터치</li>
<li>담요는 일주일에 한 번 세탁 (향 강한 세제 피하기)</li>
</ol>
<h2>페로몬 스프레이와의 차이</h2>
<p>상용 페로몬은 선택 사항입니다. <strong>담요+습관</strong>만으로도 「여기선 만져도 된다」 공간이 만들어지는 경우가 많습니다.</p>
""" + related(
            ("massage-scent-calm", "페로몬·향"),
            ("sofa-couch-massage-spot", "소파·침대"),
        ) + "<p>이 글은 <strong>냄새·담요</strong>로 터치 환경을 만드는 가이드입니다.</p>",
    },
    {
        "id": "tail-language-during-massage",
        "category": "꼬리·표현",
        "emoji": "🐈",
        "title": "마사지 중 꼬리 움직임 — 계속해도 될까, 멈출까",
        "summary": "꼬리 끝만 흔들림 vs 전체 휘둘림. 터치 중 꼬리로 읽는 실전 표.",
        "tags": ["꼬리", "표현", "신호", "마사지"],
        "content": """
<p class="article-lead">골골송이 나와도 꼬리가 <strong>세게 휘둘리면</strong> 멈춰야 할 때가 있습니다. 소리와 꼬리를 같이 봐야 합니다.</p>
<h2>대략적인 해석 (개체마다 다름)</h2>
<table class="article-table">
<tr><th>꼬리</th><th>의미 힌트</th><th>행동</th></tr>
<tr><td>끝만 살랑</td><td>집중·관심</td><td>속도 유지</td></tr>
<tr><td>천천히 좌우</td><td>편안·졸림</td><td>계속 OK</td></tr>
<tr><td>크게 휘둘림</td><td>과자극·불편</td><td>멈춤</td></tr>
<tr><td>꼬리 세움+떨림</td><td>흥분</td><td>1분 후 재시도</td></tr>
</table>
<p>표는 참고용입니다. <strong>그 고양이의 평소</strong>와 비교하는 게 가장 정확합니다.</p>
""" + related(
            ("cat-body-language-massage", "몸짓 읽기"),
            ("pain-signals-stop-massage", "중단 기준"),
        ) + "<p>이 글은 <strong>꼬리·표현</strong> 관점의 실전 가이드입니다.</p>",
    },
    {
        "id": "before-after-meal-massage-timing",
        "category": "식사·타이밍",
        "emoji": "🍽️",
        "title": "밥 전·후 언제 마사지? — 소화·기분 고려 타이밍",
        "summary": "밥그릇 앞 5분, 식후 30분. 식사와 마사지·간식 루틴을 섞지 않게 정리.",
        "tags": ["식사", "타이밍", "소화", "루틴"],
        "content": """
<p class="article-lead">「간식 주면서 만지면 좋아하지 않을까?」— <strong>식사·간식·마사지</strong> 순서가 엉키면 나중에 손만 보면 밥만 달라는 패턴이 생기기도 합니다.</p>
<h2>추천 타이밍</h2>
<ul>
<li><strong>밥 10분 전</strong> — 짧은 볼·목 터치로 「곧 밥」 예고 (1~2분)</li>
<li><strong>식후 30~60분</strong> — 소화 후 등·옆구리 5분</li>
<li><strong>간식</strong> — 마사지 ‘끝’에 아주 작게 (매번 X)</li>
</ul>
<h2>식후 바로 눕기 싫어하는 고양이</h2>
<p>식후 곧바로 배·옆구리를 건드리면 싫어할 수 있습니다. 그루밍·화장실·물 마시기 후가 더 낫습니다.</p>
""" + related(
            ("massage-and-treats", "간식+마사지"),
            ("massage-frequency-timing", "빈도·시간"),
        ) + "<p>이 글은 <strong>식사·타이밍</strong> 관점의 루틴 가이드입니다.</p>",
    },
    {
        "id": "whisker-stress-cat-face-massage",
        "category": "수염·얼굴",
        "emoji": "🎋",
        "title": "수염·볼 주변 — ‘얼굴 마사지’의 안전한 범위",
        "summary": "수염을 당기지 않고, 볼·턱·이마만 다루는 얼굴 터치 가이드.",
        "tags": ["수염", "볼", "얼굴", "터치"],
        "content": """
<p class="article-lead">고양이 얼굴은 <strong>수염·따뜻한 볼</strong> 때문에 만지고 싶지만, 수염을 잡아당기면 금방 신뢰가 깨집니다.</p>
<h2>안전한 얼굴 루틴 3분</h2>
<ol>
<li>이마 → 볼 윗부분 (수염 밖쪽) 1분</li>
<li>턱 밑·귀 뒤 1분</li>
<li>코 끝은 건드리지 않고 30초 멈춤 관찰</li>
</ol>
<p>골골송·눈 감기·앞발로 만지기 → 긍정 신호. 귀를 뒤로 젖히고 입 벌리기 → 중단.</p>
""" + related(
            ("chin-ear-massage", "턱·귀"),
            ("stroking-technique-basics", "스트로킹 기법"),
        ) + "<p>이 글은 <strong>수염·얼굴</strong> 터치 가이드입니다.</p>",
    },
    {
        "id": "cat-cafe-style-home-massage-corner",
        "category": "공간·코너",
        "emoji": "🏡",
        "title": "집 안 ‘캣 라운지’ 한 구석 — 마사지 전용 코너 만들기",
        "summary": "캣타워·소파 글과 다른, 작은 코너·매트·조명으로 ‘터치 존’을 만드는 방법.",
        "tags": ["공간", "코너", "환경", "루틴"],
        "content": """
<p class="article-lead">집 전체가 고양이 영역이지만, <strong>「여기선 항상 천천히」</strong>인 구역이 있으면 마사지가 습관화되기 쉽습니다.</p>
<h2>코너 구성 예시</h2>
<ul>
<li>창가 아닌 조용한 벽면 1㎡</li>
<li>미끄럼 방지 매트 + 얇은 담요</li>
<li>따뜻한 간접 조명 (눈부심 X)</li>
<li>브러시·물그릇을 같은 구역에</li>
</ul>
<p>매일 저녁 8시, 그 코너에서 5분—고양이가 먼저 와서 기다리는 날이 오면 성공에 가깝습니다.</p>
""" + related(
            ("cattree-massage-spot", "캣타워 옆"),
            ("pre-massage-preparation", "마사지 전 준비"),
        ) + "<p>이 글은 <strong>공간·코너</strong> 설계 가이드입니다.</p>",
    },
    {
        "id": "cat-foam-mat-massage-comfort",
        "category": "매트·쿠션",
        "emoji": "🧩",
        "title": "캣폼·매트 위 마사지 — 미끄럼·관절 부담 줄이기",
        "summary": "바닥·타일 vs 캣폼·요. 고양이·노묘·관절에 맞는 받침 선택.",
        "tags": ["매트", "캣폼", "편안", "관절"],
        "content": """
<p class="article-lead">차가운 타일 위에서 마사지하면 <strong>긴장한 채</strong> 버티는 고양이가 많습니다. 받침 하나 바꿔도 터치 시간이 늘어납니다.</p>
<h2>매트 선택 포인트</h2>
<ul>
<li>미끄럼 방지 (고양이·집사 모두)</li>
<li>너무 두꺼운 쿠션은 균형 잃기 쉬움</li>
<li>세탁 가능·털 잘 빠짐</li>
</ul>
<h2>노묘·관절</h2>
<p>낮은 캣폼+매트 조합으로 <strong>뛰어오르기 없이</strong> 코너에 올 수 있게 하면, 마사지 ‘전’ 스트레스가 줄어듭니다.</p>
""" + related(
            ("arthritis-senior-cat-joint-massage", "관절·시니어"),
            ("cat-cafe-style-home-massage-corner", "마사지 코너"),
        ) + "<p>이 글은 <strong>매트·쿠션</strong> 선택 가이드입니다.</p>",
    },
    {
        "id": "dental-gum-area-avoid-massage",
        "category": "구강·주의",
        "emoji": "🦷",
        "title": "입·잇몸·턱 아래 — 마사지와 구강 케어 구분하기",
        "summary": "턱 밑은 OK, 입 안·잇몸 직접 터치는 X. 구내염·치석과 마사지 역할 나누기.",
        "tags": ["구강", "잇몸", "턱", "주의"],
        "content": """
<p class="article-lead">턱 밑 스트로킹은 많은 고양이가 좋아하지만, <strong>입 안·잇몸</strong>은 마사지 영역이 아닙니다.</p>
<h2>구분표</h2>
<ul>
<li>턱 밑·볼 아래 — 가벼운 스트로킹 가능</li>
<li>입술 안쪽·잇몸 — 전용 칫솔·수의사</li>
<li>구취·침 흘림 증가 — 진료 우선</li>
</ul>
<p>구강 불편한 고양이는 얼굴 터치 전체를 싫어할 수 있습니다. 몸·등 위주로 짧게.</p>
""" + warn("잇몸 출혈·식사 거부 → 마사지보다 구강 검진.") + related(
            ("forbidden-zones-cat", "금지 부위"),
            ("whisker-stress-cat-face-massage", "얼굴 터치"),
        ) + "<p>이 글은 <strong>구강·주의</strong> 구분 가이드입니다.</p>",
    },
    {
        "id": "noise-sensitivity-cat-massage",
        "category": "소리·민감",
        "emoji": "🔇",
        "title": "소리·공사·천둥 날 — 고양이 마사지로 안정 돕기",
        "summary": "큰 소리·낯선 소음 후. 조용한 방·담요·짧은 터치로 긴장 낮추기.",
        "tags": ["소리", "민감", "불안", "안정"],
        "content": """
<p class="article-lead">공사·천둥·이웃 소음 뒤엔 <strong>숨기·공격성</strong>이 올라가는 고양이가 있습니다. 이때 긴 마사지보다 「안전 신호」가 먼저입니다.</p>
<h2>소음 스트레스 후 5분</h2>
<ol>
<li>안쪽 방·서랍·침대 밑 등 고양이가 고른 곳 존중</li>
<li>문 닫고 TV·음악 끄기</li>
<li>고양이가 나온 뒤 볼·목 2분, 등 3분</li>
</ol>
<p>억지로 꺼내서 만지지 마세요. <strong>스스로 나온 뒤</strong>가 효과적입니다.</p>
""" + related(
            ("anxious-cat-massage", "예민한 고양이"),
            ("moving-stress-massage", "환경 변화"),
        ) + "<p>이 글은 <strong>소리·민감</strong> 환경에서의 터치입니다.</p>",
    },
    {
        "id": "dog-cat-household-massage-separate",
        "category": "견·다견 동거",
        "emoji": "🐕",
        "title": "강아지·고양이 같이 키울 때 — 마사지는 ‘따로’",
        "summary": "냄새·영역·질투. 다른 방에서 고양이만 5분, 강아지는 다른 시간.",
        "tags": ["강아지", "다견", "동거", "분리"],
        "content": """
<p class="article-lead">강아지가 관심을 끊지 않으면 고양이는 <strong>긴장한 채</strong> 마사지를 받습니다. ‘함께’보다 ‘분리’가 먼저입니다.</p>
<h2>실전 순서</h2>
<ul>
<li>강아지 산책·놀이 후 고양이 방문</li>
<li>문 닫고 5분 터치 (강아지 짖음 최소화)</li>
<li>손·담요 냄새 바꾸기 (견 냄새 민감한 고양이)</li>
</ul>
<p>다묘 가정 글과 비슷하지만, 여기서는 <em>견+고양이</em> 조합에 초점을 둡니다.</p>
""" + related(
            ("multi-cat-household-massage", "다묘 가정"),
            ("scent-memory-cat-massage-blanket", "담요·냄새"),
        ) + "<p>이 글은 <strong>견·다견 동거</strong> 환경 가이드입니다.</p>",
    },
    {
        "id": "newly-adopted-cat-touch-timeline",
        "category": "입양·적응",
        "emoji": "🏠",
        "title": "입양 첫달 터치 타임라인 — 1주·2주·4주 마사지",
        "summary": "새 집 적응기. 보기만→손등→볼→등. 입양 고양이 신뢰 쌓는 단계별 터치.",
        "tags": ["입양", "적응", "신뢰", "타임라인"],
        "content": """
<p class="article-lead">입양 직후 「빨리 친해지고 싶다」는 마음이 <strong>과한 터치</strong>로 이어지기 쉽습니다. 예민한 고양이 글보다, <em>첫 4주 일정</em>에 맞춰 정리했습니다.</p>
<h2>대략적인 타임라인 (개체·경력마다 다름)</h2>
<ul>
<li><strong>1주</strong> — 같은 방 공존, 손등만, 눈 맞춤·천천히 깜빡임</li>
<li><strong>2주</strong> — 볼·턱 30초, 싫으면 즉시 중단</li>
<li><strong>3~4주</strong> — 목·등 2~3분, 담요 코너 고정</li>
</ul>
<p>숨기·공격·식사 거부가 지속되면 마사지보다 <strong>환경·수의사</strong> 상담이 우선입니다.</p>
""" + related(
            ("anxious-cat-massage", "예민한 고양이"),
            ("kitten-massage-intro", "새끼 고양이"),
        ) + "<p>이 글은 <strong>입양·적응</strong> 단계별 터치 가이드입니다.</p>",
    },
    {
        "id": "travel-return-cat-reunion-massage",
        "category": "여행·재회",
        "emoji": "✈️",
        "title": "여행·출장 다녀온 뒤 — 고양이와 ‘다시 만난’ 10분",
        "summary": "집사 냄새·부재 스트레스 후. 재회 10분을 급하게 끌어안지 않는 마사지.",
        "tags": ["여행", "출장", "재회", "부재"],
        "content": """
<p class="article-lead">며칠 비운 뒤 문을 열면 <strong>붙었다가 물거나, 반대로 외면</strong>하는 고양이가 있습니다. 둘 다 ‘부재’ 반응일 수 있습니다.</p>
<h2>재회 10분</h2>
<ol>
<li>짐·외투 정리, 손 씻기 (2분)</li>
<li>손등 냄새 맞추기, 볼·턱만 (3분)</li>
<li>고양이가 원하면 등·옆구리 (5분)</li>
</ol>
<p>「보고 싶었어」로 꽉 안기보다, <strong>예전 루틴 그대로</strong>가 더 빨리 일상으로 돌아갑니다.</p>
<h2>펫시터·병원과의 차이</h2>
<p>낯선 사람이 돌봤다면 재적응에 며칠 더 걸릴 수 있습니다. 짧게·자주가 길게·한 번보다 낫습니다.</p>
""" + related(
            ("vet-visit-recovery-massage", "병원 후"),
            ("commute-stress-cat-welcome-massage", "퇴근 환영"),
        ) + "<p>이 글은 <strong>여행·재회</strong> 관점의 터치 가이드입니다.</p>",
    },
]


def main() -> None:
    data = json.loads(POSTS_PATH.read_text(encoding="utf-8"))
    existing_cats = {p.get("category") for p in data["posts"]}
    existing_ids = {p.get("id") for p in data["posts"]}

    added = 0
    for spec in NEW_POSTS:
        if spec["category"] in existing_cats:
            raise ValueError(f"duplicate category: {spec['category']}")
        if spec["id"] in existing_ids:
            raise ValueError(f"duplicate id: {spec['id']}")
        existing_cats.add(spec["category"])
        existing_ids.add(spec["id"])
        data["posts"].insert(
            0,
            {
                "id": spec["id"],
                "title": spec["title"],
                "summary": spec["summary"],
                "category": spec["category"],
                "content": spec["content"].strip(),
                "tags": spec["tags"],
                "author": "고양이",
                "date": TODAY,
                "emoji": spec["emoji"],
                "published": True,
            },
        )
        added += 1

    POSTS_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Added {added} posts dated {TODAY}")
    print("New categories:", [p["category"] for p in NEW_POSTS])


if __name__ == "__main__":
    main()
