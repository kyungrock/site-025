#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""고양이 마사지 신규 10편 — 카테고리 중복 없음, 2026-07-14"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_PATH = ROOT / "data" / "blog-posts.json"
TODAY = "2026-07-14"


def tip(t: str) -> str:
    return f'<div class="tip-box">\n<strong>팁</strong>\n{t}\n</div>'


def warn(t: str) -> str:
    return f'<div class="warn-box">\n<strong>주의</strong>\n{t}\n</div>'


def related(*links: tuple[str, str]) -> str:
    items = "".join(
        f'<li><a href="{hid}.html">{title}</a></li>' for hid, title in links
    )
    return f"<h2>함께 읽으면 좋은 글</h2>\n<ul>\n{items}\n</ul>"


NEW_POSTS = [
    {
        "id": "rainy-day-indoor-cat-massage",
        "category": "비·실내날",
        "emoji": "🌧️",
        "title": "비 오는 날 실내 고양이 마사지 — 창밖 소리와 이완 루틴",
        "summary": "장마·빗소리에 예민한 반려묘를 위한 실내 이완. 닫힌 창문·담요·천천히 스트로킹하는 15분 가이드.",
        "tags": ["비오는날", "장마", "실내", "고양이마사지", "이완"],
        "content": f"""
<p class="article-lead">창문에 빗방울이 떨어지는 날, 고양이가 <strong>창가에 붙었다가 갑자기 숨기</strong>를 반복하는 집이 많습니다. 외부 소리·기압 변화에 예민한 날에는 짧게·조용하게·익숙한 자리에서만 터치하는 게 핵심입니다.</p>
<h2>비 오는 날, 마사지가 ‘방해’가 될 때</h2>
<p>바깥 소음이 크면 고양이는 귀를 뒤로 젖히거나, 눈만 크게 뜨고 몸을 웅크리는 경우가 있습니다. 이때 억지로 끌어내 쓰다듬으면 <strong>긴장만 쌓입니다</strong>. 먼저 커튼을 반쯤 치고, TV·청소기 소리를 줄인 뒤, 고양이가 스스로 다가올 때까지 기다리는 편이 낫습니다.</p>
<p>20~50대 마사지·힐링·웰니스에 관심 있는 집사라면, 비가 올 때를 「강제 애정 시간」이 아니라 <strong>환경 조절 + 짧은 터치</strong>로 생각하면 부담이 덜합니다.</p>
<h2>15분 실내 이완 루틴</h2>
<ol>
<li><strong>2분</strong> — 방 문을 닫고 조명만 약하게. 손 씻고 체온을 맞춤.</li>
<li><strong>3분</strong> — 손등만 내밀어 냄새 맞추기. 반응 없으면 여기서 종료.</li>
<li><strong>5분</strong> — 볼·턱·목 뒤 스트로킹. 빗소리에 귀가 움직일 때마다 속도 더 느리게.</li>
<li><strong>3분</strong> — 등 중앙→옆구리. 꼬리가 크게 휘둘리면 즉시 멈춤.</li>
<li><strong>2분</strong> — 손으로 담요를 덮지 말고, 옆에 두어 스스로 눕게 두기.</li>
</ol>
{tip("장마철엔 습도가 올라가도 에어컨 바람이 피부를 마르게 하니, 손 마사지 전 가벼운 브러시만으로도 충분할 때가 많습니다.")}
{warn("천둥·번개에는 숨기 공간을 먼저 확보하세요. 억지 터치보다 안전이 우선입니다.")}
{related(("noise-sensitivity-cat-massage", "소리·민감 마사지"), ("scent-memory-cat-massage-blanket", "담요·자리 만들기"))}
<p>이 글은 <strong>비·실내날</strong> 관점에서 고양이 마사지·이완을 정리한 정보성 콘텐츠입니다. 수의 진료를 대체하지 않습니다.</p>
""",
    },
    {
        "id": "nail-trim-aftercare-massage",
        "category": "발톱·그루밍후",
        "emoji": "✂️",
        "title": "발톱 깎은 뒤 고양이 마사지 — 거부감 줄이는 애프터케어",
        "summary": "발톱 손질 직후 긴장을 풀는법. 발 패드를 바로 건드리지 않고 머리·목부터 풀어주는 순서.",
        "tags": ["발톱깎기", "그루밍", "애프터케어", "고양이마사지"],
        "content": f"""
<p class="article-lead">발톱을 깎는 날은 고양이와 집사 모두 <strong>힘과 긴장이 올라가는</strong> 날입니다. 「발 마사지로 보상」하려다 오히려 발만 보면 도망가게 만드는 경우도 있어요.</p>
<h2>발톱 손질 후 바로 하면 안 되는 것</h2>
<ul>
<li>발바닥·발가락 사이를 바로 주무르기</li>
<li>「다 끝났으니」라며 길게 안고 있기</li>
<li>간식만 주고 몸을 꽉 끌어안기</li>
</ul>
<p>발은 방금 ‘다루어진 부위’라서, 당분간은 <strong>머리·볼·목·등</strong>처럼 익숙하고 안전한 구간에서 신뢰를 회복하는 편이 좋습니다.</p>
<h2>10분 애프터케어 순서</h2>
<ol>
<li>장소 바꾸기 — 발톱 깎던 자리와 다른 담요·소파로 이동 (2분)</li>
<li>볼·턱만 1~2분. 골골송이 나오는지 확인</li>
<li>목 뒤→어깨 윗등 3분</li>
<li>옆구리만 가볍게. 발 쪽은 손이 가지 않게</li>
<li>스스로 그루밍할 시간을 줌</li>
</ol>
{tip("발톱 손질은 ‘짧은 간격·짧게 끝내기’가 마사지 학습에도 유리합니다. 한 번에 네 발 다 무리하게 하지 않아도 됩니다.")}
{related(("paw-pad-massage", "발·발가락 마사지"), ("post-bath-massage-cat", "목욕 후 마사지"))}
<p>이 글은 <strong>발톱·그루밍후</strong> 이완 케어 정보입니다.</p>
""",
    },
    {
        "id": "pregnant-cat-gentle-massage-caution",
        "category": "임신·출산케어",
        "emoji": "🍼",
        "title": "임신한 고양이 마사지 — 가능 부위와 절대 금기",
        "summary": "임신묘 웰니스. 복부·허리 압을 피하고 볼·목만 짧게. 수의사 확인이 우선인 이유.",
        "tags": ["임신고양이", "출산", "안전", "마사지주의"],
        "content": f"""
<p class="article-lead">임신한 고양이에게 터치로 안정을 주고 싶은 마음은 자연스럽습니다. 다만 <strong>‘이완’과 ‘위험’의 경계</strong>가 좁기 때문에, 일반 마사지 루틴을 그대로 가져오면 안 됩니다.</p>
<h2>원칙: 복부·허리 깊은 압은 금지</h2>
<p>임신 중기 이후 배가 불러오면 옆구리·복부 아래를 누르는 스트로킹은 피하세요. 집사가 「부드럽게」라고 느껴도, 복압·스트레스로 이어질 수 있습니다. 자궁·태아 관련 이슈는 마사지로 해결할 영역이 아닙니다.</p>
<h2>해도 되는 범위 (짧은 접촉)</h2>
<ul>
<li>볼·턱·이마 — 냄새 맞추며 30초~2분</li>
<li>목 뒤 아주 가볍게 (아래쪽으로 강하게 쓸어내리지 않기)</li>
<li>머리만 쓰다듬고 몸을 억지로 눕히지 않기</li>
</ul>
{warn("식욕 급감, 무기력, 출혈·분비물, 극심한 숨기 등 변화가 있으면 마사지를 중단하고 즉시 수의사와 상담하세요.")}
{tip("임신·출산 전후는 ‘터치 습관’보다 온습도·은신처·깨끗한 화장실이 우선입니다.")}
{related(("forbidden-zones-cat", "금지 부위"), ("pain-signals-stop-massage", "중단 신호"))}
<p>이 글은 <strong>임신·출산케어</strong> 관점의 안전 안내이며 의료 조언이 아닙니다.</p>
""",
    },
    {
        "id": "carrier-crate-calming-massage",
        "category": "이동장·트레이닝",
        "emoji": "🧳",
        "title": "이동장 익히기 + 마사지 — 병원 가기 전 카밍 루틴",
        "summary": "이동장을 공포 공간에서 안전 공간으로. 문 연 상태에서 볼 터치로 연합시키는 3주 연습법.",
        "tags": ["이동장", "캐리어", "병원가기", "카밍", "훈련"],
        "content": f"""
<p class="article-lead">병원·미용·여행 전에 이동장만 보이면 숨는 고양이가 많습니다. 「억지로 넣고 보상」만 반복하면 이동장은 계속 <strong>나쁜 기억</strong>으로 남습니다. 마사지를 이동장과 <em>좋은 연합</em>으로 쓰는 방법을 정리했습니다.</p>
<h2>3주 연습 스케치</h2>
<ol>
<li><strong>1주</strong> — 뚜껑·문을 열어 둔 채 담요·간식을 넣고, 집사는 옆에만 앉음. 터치 없음도 OK.</li>
<li><strong>2주</strong> — 이동장 안에서 머리를 내밀면 볼·턱만 10~30초.</li>
<li><strong>3주</strong> — 몸이 반쯤 들어간 뒤 목을 가볍게. 문을 잠시 닫았다 즉시 여는 연습은 아주 짧게.</li>
</ol>
<p>핵심은 속도가 아니라 <strong>고양이가 선택권을 갖는 것</strong>입니다. 손을 안으로 뻗어 억지로 끌어내면 학습이 깨집니다.</p>
{tip("병원 전날 밤, 이동장을 ‘마사지 코너’처럼 같은 자리에 미리 꺼내 두면 당일 거부감이 줄어드는 집이 많습니다.")}
{related(("vet-visit-recovery-massage", "병원 후 마사지"), ("pre-massage-preparation", "마사지 전 준비"))}
<p>이 글은 <strong>이동장·트레이닝</strong>과 이완 터치를 연결한 가이드입니다.</p>
""",
    },
    {
        "id": "allergy-season-cat-massage-dust",
        "category": "알레르기·먼지",
        "emoji": "🤧",
        "title": "환절기 먼지·알레르기 시즌 — 집사·고양이 둘 다 편한 터치법",
        "summary": "미세먼지·꽃가루 시즌. 브러시 후 손 씻기, 짧은 마사지, 환기 타이밍을 맞추는 웰니스 팁.",
        "tags": ["알레르기", "미세먼지", "환절기", "고양이마사지", "셀프케어"],
        "content": f"""
<p class="article-lead">환절기엔 고양이의 털·먼지와 집사의 알레르기가 겹치기 쉽습니다. 「마사지하고 싶은데 재채기가 나서」 손이 멈추는 날, <strong>순서만 바꿔도</strong> 부담을 줄일 수 있습니다.</p>
<h2>먼지 시즌 권장 순서</h2>
<ol>
<li>창을 잠시 닫고 HEPA 필터·청소기(고양이가 없을 때) 사용</li>
<li>브러시로 표면 털 2분 (야외 환기 직후는 피하기)</li>
<li><strong>손 씻기</strong> 후 볼·목 마사지 5분</li>
<li>끝난 뒤 옷·무릎 털을 즉시 제거</li>
</ol>
<p>마사지·힐링·웰니스를 동시에 챙기려면, 하루 20분 긴 세션보다 <strong>5분×2회</strong>가 집사 호흡기에도, 고양이 자극에도 낫습니다.</p>
{warn("고양이 재채기·눈곱·호흡 소리가 갑자기 늘면 환경 문제인지 호흡기 질환인지 구분이 필요합니다. 자가 마사지로 해결하려 하지 마세요.")}
{related(("shedding-season-massage-brush", "털갈이철 마사지"), ("brush-massage-combo", "브러시+마사지"))}
<p>이 글은 <strong>알레르기·먼지</strong> 시즌 터치 팁입니다.</p>
""",
    },
    {
        "id": "window-perch-height-massage-safe",
        "category": "창가·높은곳",
        "emoji": "🪟",
        "title": "창가·캣퍼치에서의 마사지 — 높이·균형·떨어짐 주의",
        "summary": "높은 곳에서 만지면 놀란 고양이가 뛰어내릴 수 있습니다. 바닥·안정 자세일 때만 터치하는 기준.",
        "tags": ["창가", "캣퍼치", "안전", "균형", "마사지"],
        "content": f"""
<p class="article-lead">창가에 앉아 골골송을 내는 모습을 보면 바로 쓰다듬고 싶어집니다. 다만 <strong>높이 + 갑작스러운 손</strong>은 균형 실수를 만듭니다. 창가·캣타워에서의 터치 규칙을 따로 정해 두면 사고가 줄어듭니다.</p>
<h2>높은 곳에서 지켜야 할 규칙</h2>
<ul>
<li>몸이 완전히 앉거나 누운 <strong>안정 자세</strong>일 때만</li>
<li>머리·볼만. 등을 세게 누르면 앞으로 쏠릴 수 있음</li>
<li>손 하나에만 체중을 싣지 않기</li>
<li>불안하면 먼저 내려오도록 유도한 뒤 바닥에서 마사지</li>
</ul>
<p>「창가에서만 친해진다」는 패턴이 있다면, 바닥 매트에서도 같은 손길을 연습해 보세요. 높은 곳이 ‘유일한 안전’이 되지 않게 하는 게 장기적으로 유리합니다.</p>
{tip("창가 난간·선반이 좁으면 마사지 금지 구역으로 두는 것도 방법입니다.")}
{related(("cattree-massage-spot", "캣타워 옆"), ("cat-foam-mat-massage-comfort", "매트 위 마사지"))}
<p>이 글은 <strong>창가·높은곳</strong> 안전 터치 가이드입니다.</p>
""",
    },
    {
        "id": "left-handed-owner-cat-massage",
        "category": "손잡이·습관",
        "emoji": "👈",
        "title": "왼손잡이 집사 고양이 마사지 — 각도·방향 맞추는 법",
        "summary": "주로 쓰는 손·앉는 방향에 따라 고양이 반응도 달라집니다. 왼손잡이·양손 쓰기 실전 팁.",
        "tags": ["왼손잡이", "손습관", "스트로킹", "자세"],
        "content": f"""
<p class="article-lead">인터넷 가이드의 「오른손으로 쓸어내리기」  orth을 따르다 보면 왼손잡이 집사는 어깨가 먼저 굳습니다. 중요한 건 어느 손이냐가 아니라 <strong>고양이가 예측 가능한 한 방향·일정한 압력</strong>입니다.</p>
<h2>왼손잡이에게 편한 세팅</h2>
<ol>
<li>고양이를 몸 왼쪽에 두고 앉기 (시야·팔 각도가 자연스러움)</li>
<li>비주력 손은 어깨·골반 옆을 ‘받치는’ 용도로만 (누르지 않기)</li>
<li>주력 손으로 이마→목→등 한 방향 스트로크</li>
</ol>
<p>방향을 자주 바꾸면 고양이는 ‘다음에 어디로 손 올지’ 긴장합니다. <strong>오늘은 왼쪽에서 오른쪽으로만</strong>처럼 규칙을 단순화하세요.</p>
{tip("손목이 아프면 손가락 끝이 아니라 손바닥 면을 더 쓰세요. 마사지 도구(글러브)는 주력 손 위주로.")}
{related(("stroking-technique-basics", "스트로킹 기법"), ("hand-warmth-touch-cat", "손 체온 준비"))}
<p>이 글은 <strong>손잡이·습관</strong> 관점의 실전 마사지입니다.</p>
""",
    },
    {
        "id": "vacation-pet-sitter-massage-handoff",
        "category": "펫시터·인수인계",
        "emoji": "🤝",
        "title": "펫시터에게 넘기는 고양이 마사지 인수인계 메모",
        "summary": "여행·출장 전. ‘어디서·몇 분·어디가 싫다’를 시터에게 전하는 체크리스트와 터치 원칙.",
        "tags": ["펫시터", "인수인계", "여행", "체크리스트"],
        "content": f"""
<p class="article-lead">집을 비울 때 「평소처럼 쓰다듬어 주세요」만으로는 부족합니다. 시터마다 손길이 다르고, 고양이는 <strong>낯선 사람 + 낯선 압</strong>에 바로 반응합니다.</p>
<h2>인수인계에 넣을 항목</h2>
<ul>
<li>좋아하는 부위 / 절대 건드리지 말 부위</li>
<li>하루 권장 시간(예: 저녁 5분, 볼·목만)</li>
<li>싫어할 때 신호(꼬리·귀·물기 징조)</li>
<li>마사지 자리(담요·방)</li>
<li>병원·비상 연락처</li>
</ul>
<p>시터에게 ‘오래 안고 있기’는 부탁하지 않는 편이 안전합니다. <strong>짧게·머리 위주·거부 시 즉시 중단</strong>만 적어도 재회 후 회복이 빨라집니다.</p>
{related(("travel-return-cat-reunion-massage", "여행 후 재회"), ("cat-body-language-massage", "신호 읽기"))}
<p>이 글은 <strong>펫시터·인수인계</strong>용 실용 메모입니다.</p>
""",
    },
    {
        "id": "autumn-first-chill-cat-massage",
        "category": "환절기·첫추위",
        "emoji": "🍁",
        "title": "가을 첫추위 — 체온 떨어지고 뻣뻣해진 고양이 풀기",
        "summary": "갑자기 쌀쌀해진 밤. 담요·방 온도·짧은 등 마사지로 근육 긴장을 풀어주는 환절기 케어.",
        "tags": ["가을", "환절기", "첫추위", "이완", "웰니스"],
        "content": f"""
<p class="article-lead">여름이 가시고 첫 선선한 바람이 불면, 고양이가 <strong>웅크리거나 움직임이 줄어드는</strong> 집이 있습니다. 겨울 건조·털갈이 주제와 겹치지 않게, 여기서는 ‘갑자기 추워진 며칠’만 다룹니다.</p>
<h2>첫추위 3일 케어</h2>
<ol>
<li>방 온도를 급격히 올리지 말고, 차가운 코너를 막기</li>
<li>마사지 전 담요를 살짝 따뜻하게(전자레인지 과열 X, 체온 정도)</li>
<li>등·어깨 윗부분만 5~7분. 배·발은 생략</li>
<li>마사지 후 바로 창가 통풍에 두지 않기</li>
</ol>
<p>노묘·관절이 예민한 아이는 특히 「바닥이 차가워진 느낌」에 민감합니다. 매트 위에서만 터치하세요.</p>
{related(("arthritis-senior-cat-joint-massage", "관절·시니어"), ("winter-dry-skin-massage", "겨울 건조"))}
<p>이 글은 <strong>환절기·첫추위</strong> 이완 가이드입니다.</p>
""",
    },
    {
        "id": "smartphone-break-cat-touch-habit",
        "category": "폰·스크린타임",
        "emoji": "📱",
        "title": "스마트폰 내려놓고 3분 — 스크롤 대신 고양이 마사지 습관",
        "summary": "잠들기 전·점심 후 폰을 보는 시간을 터치 루틴으로 바꾸는 현실적인 습관 설계.",
        "tags": ["스마트폰", "습관", "디톡스", "고양이마사지", "셀프케어"],
        "content": f"""
<p class="article-lead">「여유가 없어서 마사지를 못 한다」기보다, <strong>폰을 보는 3분</strong>이 이미 있는 집이 많습니다. 그 조각을 옮기면 새로운 시간을 만들 필요가 없습니다.</p>
<h2>트리거·행동·보상</h2>
<ul>
<li><strong>트리거</strong> — 알람, 충전 케이블 꽂기, 소파에 앉기</li>
<li><strong>행동</strong> — 폰은 뒤집어 두고, 고양이 볼·목 3분</li>
<li><strong>보상</strong> — 끝난 뒤 물 한 잔·짧은 스트레칭 (집사 셀프케어)</li>
</ul>
<p>매일 완벽할 필요는 없습니다. 주 4회만 해도 고양이는 「이 시간에 손이 온다」고 예측하기 시작합니다. 마사지·힐링·웰니스를 거창한 루틴이 아니라 <strong>스크린타임 대체</strong>로 접근해 보세요.</p>
{tip("알림을 끄기 어렵다면 ‘방해금지 3분’만 위젯으로 두어도 충분합니다.")}
{related(("evening-cat-massage-routine", "저녁 루틴"), ("self-care-massage-link", "집사 셀프케어 연계"))}
<p>이 글은 <strong>폰·스크린타임</strong>을 이완 터치로 바꾸는 습관 가이드입니다.</p>
""",
    },
]


def main() -> None:
    data = json.loads(POSTS_PATH.read_text(encoding="utf-8"))
    existing_cats = {p.get("category") for p in data["posts"]}
    existing_ids = {p.get("id") for p in data["posts"]}

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

    POSTS_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Added {len(NEW_POSTS)} posts dated {TODAY}")
    for p in NEW_POSTS:
        print(f"  - [{p['category']}] {p['title']}")


if __name__ == "__main__":
    main()
