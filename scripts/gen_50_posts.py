#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""고양이 마사지 SEO 블로그 50편 생성 → data/blog-posts.json"""

from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "blog-posts.json"


def body(*parts: str) -> str:
    return "\n".join(parts)


def tip(text: str) -> str:
    return f'<div class="tip-box">\n<strong>팁</strong>\n{text}\n</div>'


def warn(text: str) -> str:
    return f'<div class="warn-box">\n<strong>주의</strong>\n{text}\n</div>'


def sec(title: str, *paras: str) -> str:
    chunks = [f"<h2>{title}</h2>"]
    for p in paras:
        if p.startswith("<"):
            chunks.append(p)
        else:
            chunks.append(f"<p>{p}</p>")
    return "\n".join(chunks)


POST_SPECS: list[tuple] = [
    (
        "cat-massage-complete-guide",
        "입문·기초",
        "🐱",
        "고양이 마사지 완벽 가이드 — 처음 시작하는 집사를 위한 입문",
        "고양이 마사지의 원리, 효과, 시작 전 준비를 SEO 친화적으로 정리한 입문 가이드. 이완·유대감의 기초를 한곳에.",
        "고양이마사지,입문,이완,웰니스",
        lambda: body(
            "<p><strong>고양이 마사지</strong>는 손끝으로 천천히 쓰다듬어 반려묘의 긴장을 낮추고 유대감을 쌓는 셀프케어입니다. 마사지·힐링·웰니스에 관심 있는 20~50대 집사에게 특히 잘 맞아요.</p>",
            sec(
                "고양이 마사지란?",
                "목·등·볼·턱 등 고양이가 편안해하는 부위를 가볍게 스트로킹하는 터치입니다.",
                "강한 압이 아니라 <strong>느리고 일정한 리듬</strong>이 핵심이에요.",
            ),
            sec(
                "시작 3단계",
                "<ol><li>고양이가 편한 자세인지 확인합니다</li><li>볼·목 뒤부터 30초 가볍게 쓰다듬습니다</li><li>꼬리·배는 반응 보며 짧게 시도합니다</li></ol>",
            ),
            tip("간식보다 먼저 마사지를 하면 긍정 연상이 쌓이기 쉽습니다."),
            warn("의료 진단·치료를 대체하지 않습니다. 통증·상처가 의심되면 수의사와 상담하세요."),
        ),
    ),
    (
        "cat-body-language-massage",
        "반응 읽기",
        "👀",
        "고양이 몸짓으로 마사지 타이밍 읽기 — 좋아할 때·멈출 때",
        "꼬리·귀·눈으로 보내는 신호를 읽고, 마사지를 이어갈지 멈출지 판단하는 실전 가이드.",
        "고양이신호,마사지,반응,이완",
        lambda: body(
            "<p>마사지는 <strong>고양이가 원할 때</strong>가 가장 효과적입니다. 몸짓을 읽는 법을 알아두세요.</p>",
            sec(
                "계속해도 좋은 신호",
                "<ul><li>천천히 눈 깜빡임</li><li>부드러운 골골송</li><li>마사지하는 손에 머리 비비기</li></ul>",
            ),
            sec(
                "멈춰야 할 신호",
                "<ul><li>꼬리 휘둘림·귀 뒤로 젖힘</li><li>발톱 내밀기·물기 시도</li><li>자리에서 도망가려 함</li></ul>",
            ),
            tip("싫어하면 그날은 1분만 하고 내일 다시 시도하세요."),
        ),
    ),
    (
        "stroking-technique-basics",
        "스트로킹 기법",
        "✋",
        "고양이 스트로킹 기법 — 손 위치·속도·압력",
        "한 손 vs 두 손, 느린 스트로크, 압력 조절까지. 처음부터 올바른 터치 습관을 만드는 방법.",
        "스트로킹,고양이마사지,기법,터치",
        lambda: body(
            sec(
                "기본 스트로크",
                "이마에서 목 뒤, 등 중앙으로 <strong>한 방향</strong>으로 천천히 쓸어 내립니다.",
                "왔다 갔다 빠르게 문지르지 않는 것이 좋아요.",
            ),
            sec("압력", "손바닥 전체를 평평하게 대고, 손가락 끝만 꾹 누르지 마세요."),
            tip("털이 엉키면 브러시로 먼저 정리한 뒤 마사지하면 더 편합니다."),
        ),
    ),
    (
        "neck-shoulder-cat-massage",
        "목·어깨",
        "🦴",
        "고양이 목·어깨 마사지 — 긴장 풀어주는 5분 루틴",
        "목 뒤·어깨 윗부분을 부드럽게 풀어 주는 5분 루틴. 책상에 오래 앉은 집사와 함께 이완하기 좋아요.",
        "목마사지,어깨,고양이,이완",
        lambda: body(
            "<p>고양이도 스트레스를 목·어깨에 쌓는 경우가 많습니다.</p>",
            sec("5분 루틴", "<ol><li>볼·턱 30초</li><li>목 뒤 양쪽 1분</li><li>어깨 윗등 2분</li><li>꼬리 밑부분 30초</li></ol>"),
            warn("목 앞·목덜미 깊은 압은 피하세요."),
        ),
    ),
    (
        "back-spine-massage-cat",
        "등·척추",
        "🐾",
        "고양이 등·척추 라인 마사지 — 안전한 터치 구간",
        "척추 양옆 근육을 따라가는 마사지. 척추 뼈를 직접 누르지 않는 것이 포인트입니다.",
        "등마사지,척추,고양이마사지,안전",
        lambda: body(
            sec("터치 구간", "척추 <strong>양옆 1~2cm</strong> 부드러운 근육층만 쓰다듬습니다."),
            sec("피해야 할 곳", "척추 뼈 중앙, 꼬리 뿌리 급격한 압"),
            tip("고양이가 등을 아치형으로 내밀면 잘 하고 있다는 신호예요."),
        ),
    ),
]

MORE_SPECS = [
    ("belly-side-massage-cat", "복부·옆구리", "🤰", "고양이 배·옆구리 마사지 — 허용될 때만", "배 마사지는 신뢰가 쌓인 뒤 짧게. 옆구리는 비교적 안전한 대안.", "배마사지,옆구리,신뢰,고양이"),
    ("paw-pad-massage", "발·발가락", "🐾", "고양이 발바닥·발가락 마사지 — 짧고 가볍게", "발 터치에 익숙한 고양이만 시도. 발가락 사이는 건드리지 않아요.", "발마사지,발바닥,터치,이완"),
    ("chin-ear-massage", "귀·턱", "😺", "턱·귀 밑 마사지 — 골골송 유도하는 구간", "턱 밑·귀 뒤는 많은 고양이가 좋아하는 존.", "턱,귀,골골송,마사지"),
    ("brush-massage-combo", "브러시 마사지", "🪮", "브러시와 마사지 병행 — 털·피부·이완 한 번에", "브러싱 후 손 마사지로 마무리하는 루틴.", "브러시,털관리,마사지,셀프케어"),
    ("massage-tools-cat", "마사지 도구", "🧤", "고양이 마사지 글러브·브러시 선택 가이드", "실리콘 글러브, 핀 브러시, 고무 빗 비교.", "도구,글러브,브러시,웰니스"),
    ("massage-frequency-timing", "시간·빈도", "⏱️", "고양이 마사지 빈도·시간 — 하루 몇 분이 적당할까", "하루 5~10분, 1~2회. 짧게 자주가 길게 한 번보다 낫습니다.", "빈도,시간,습관,이완"),
    ("stress-relief-cat-massage", "스트레스 완화", "😌", "스트레스 받은 고양이 마사지 — 진정 루틴", "이사·다묘·소음 후 긴장을 낮추는 천천한 터치.", "스트레스,진정,이완,힐링"),
    ("senior-cat-gentle-massage", "노령고양이", "🧓", "노령고양이 마사지 — 관절·근육을 위한 부드러운 케어", "관절이 뻣뻣한 노묘를 위한 가벼운 스트로킹.", "노묘,시니어,관절,케어"),
    ("kitten-massage-intro", "아기고양이", "🐣", "아기 고양이 마사지 — 짧은 터치로 사회화 돕기", "새끼는 1~2분, 놀이처럼 가볍게.", "새끼고양이,사회화,터치,가족케어"),
    ("multi-cat-household-massage", "다묘가정", "🏠", "다묘 가정 마사지 — 순서·공간·질투 관리", "한 마리씩 따로, 냄새 섞이지 않게.", "다묘,가족,순서,케어"),
    ("owner-relaxation-with-cat", "주인 이완", "🧘", "집사도 함께 이완 — 고양이 마사지로 셀프케어", "고양이 마사지하며 호흡을 고르면 집사도 힐링.", "셀프케어,이완,웰니스,힐링"),
    ("pre-massage-preparation", "마사지 전 준비", "🛋️", "마사지 전 준비 — 환경·손·고양이 컨디션", "조용한 공간, 손톱 정리, 간식 준비.", "준비,환경,루틴,마사지전"),
    ("post-massage-aftercare", "마사지 후 케어", "💤", "마사지 후 케어 — 물·휴식·놀이 연결", "마사지 후 졸리면 낮잠 시간을 존중하세요.", "마사지후,휴식,케어,이완"),
    ("forbidden-zones-cat", "금지 구역", "🚫", "고양이 마사지 금지 부위 — 절대 누르지 말 것", "배 중앙, 꼬리 뿌리, 발가락 사이, 항문 주변.", "금지,안전,주의,부위"),
    ("pain-signals-stop-massage", "통증 신호", "⚠️", "아픈 고양이 신호 — 마사지 중단 기준", "숨소리 변화, 핥기 증가, 숨기 행동.", "통증,신호,중단,건강"),
    ("morning-cat-massage-routine", "아침 루틴", "🌅", "아침 고양이 마사지 3분 — 하루 시작 루틴", "밥 전 가벼운 터치로 긍정 하루 시작.", "아침,루틴,습관,이완"),
    ("evening-cat-massage-routine", "저녁 루틴", "🌙", "저녁 고양이 마사지 10분 — 하루 마무리 힐링", "잠들기 전 천천한 스트로킹으로 이완.", "저녁,수면,루틴,힐링"),
    ("bedtime-massage-cat", "수면 전", "😴", "잠들기 전 고양이 마사지 — 골골송과 함께", "침대 옆에서 5분, 조명은 어둡게.", "수면,잠들기,이완,밤"),
    ("post-play-massage", "놀이 후", "🎾", "놀이 후 마사지 — 흥분을 이완으로 전환", "사냥놀이 10분 후 3분 마사지로 진정.", "놀이,진정,전환,루틴"),
    ("post-bath-massage-cat", "목욕 후", "🛁", "목욕·그루밍 후 마사지 — 피부 진정", "물기 제거 후 따뜻한 방에서 가볍게.", "목욕,그루밍,피부,진정"),
    ("vet-visit-recovery-massage", "병원 후", "🏥", "병원 다녀온 후 마사지 — 스트레스 회복", "검진·접종 후 24시간 뒤 짧게 시도.", "병원,스트레스,회복,케어"),
    ("moving-stress-massage", "환경 변화", "📦", "이사·가구 변경 후 — 불안한 고양이 마사지", "익숙한 담요 위에서 같은 루틴 유지.", "이사,불안,적응,가족케어"),
    ("winter-dry-skin-massage", "겨울 건조", "❄️", "겨울 건조기·난방 시즌 — 피부·털 마사지", "정전기 적은 시간대, 가습과 병행.", "겨울,건조,피부,시즌"),
    ("summer-heat-massage-cat", "여름 더위", "☀️", "여름 더위 — 시원한 시간대 마사지 팁", "한낮 피하고 저녁에 짧게.", "여름,더위,시즌,이완"),
    ("longhair-cat-massage", "장모종", "🦁", "장모종 고양이 마사지 — 털 엉킸 방지", "브러시→마사지 순서, 배 털 주의.", "장모,털,브러시,마사지"),
    ("shorthair-cat-massage", "단모종", "🐈", "단모종 고양이 마사지 — 손끝 감각 살리기", "짧은 털은 손의 온기가 잘 전달됩니다.", "단모,터치,마사지,이완"),
    ("overweight-cat-massage", "비만고양이", "⚖️", "비만 고양이 마사지 — 관절 부담 줄이기", "누운 자세, 등·옆구리 위주.", "비만,관절,건강,케어"),
    ("skinny-cat-massage", "마른 고양이", "🦴", "마른 고양이 마사지 — 뼈 압 주의", "뼈가 드러난 부위는 더 가볍게.", "마름,영양,터치,주의"),
    ("anxious-cat-massage", "예민한 고양이", "😿", "예민한 고양이 마사지 — 신뢰 쌓는 단계", "1주일간 볼만 터치, 점점 범위 확대.", "예민,불안,신뢰,단계"),
    ("nocturnal-cat-massage", "야행성 고양이", "🌃", "밤에 깨는 고양이 — 야행성과 마사지 타이밍", "활동 전 짧은 마사지로 과흥분 완화.", "야행,밤,타이밍,루틴"),
    ("sofa-couch-massage-spot", "소파·침대", "🛋️", "소파·침대에서 하는 고양이 마사지", "집사 옆에 앉은 뒤 자연스럽게 터치.", "소파,침대,일상,터치"),
    ("cattree-massage-spot", "캣타워 옆", "🪜", "캣타워·창가 자리 마사지", "높은 곳에서 편안할 때 목 뒤만 짧게.", "캣타워,공간,자세,마사지"),
    ("bed-massage-with-cat", "침대에서", "🛏️", "침대에서 함께 — 누워서 하는 마사지", "집사와 나란히 누워 옆구리·등 터치.", "침대,누워,이완,힐링"),
    ("massage-and-brushing", "마사지+브러싱", "✨", "브러싱 후 손 마사지 — 15분 홈 스파", "그루밍→스트로킹→휴식 3단계.", "홈스파,브러싱,루틴,웰니스"),
    ("massage-and-treats", "마사지+간식", "🍖", "간식과 마사지 — 긍정 강화 타이밍", "마사지 끝에 아주 작은 간식 한 조각.", "간식,긍정강화,훈련,유대"),
    ("massage-scent-calm", "마사지+냄새", "🌿", "페로몬·은은한 향과 마사지 (주의 포함)", "고양이용 페로몬은 선택, 인공향은 피하세요.", "페로몬,향,진정,환경"),
    ("massage-soft-music", "마사지+음악", "🎵", "잔잔한 음악과 고양이 마사지", "낮은 볼륨 클래식·자연음.", "음악,분위기,이완,힐링"),
    ("family-cat-massage", "가족 참여", "👨‍👩‍👧", "가족이 돌아가며 마사지 — 역할 나누기", "한 사람씩 3분, 고양이가 편한 사람부터.", "가족,역할,다함께,케어"),
    ("kids-cat-massage-safety", "아이와 함께", "👶", "아이와 고양이 마사지 — 안전하게 함께하기", "손등으로만, 짧게, 어른이 옆에서.", "아이,안전,가족케어,교육"),
    ("holistic-cat-wellness-hub", "웰니스 허브", "💚", "고양이 마사지 웰니스 허브 — 힐링·셀프케어 총정리", "고양이 마사지를 중심으로 마사지·힐링·웰니스 연결.", "웰니스,허브,힐링,셀프케어"),
    ("self-care-massage-link", "셀프케어 연계", "🤲", "집사 셀프 마사지 + 고양이 마사지 루틴", "손목·어깨 셀프 케어 후 고양이 터치.", "셀프케어,집사,웰니스,루틴"),
    ("healing-routine-cat", "힐링 루틴", "💆", "주말 20분 고양이 힐링 루틴", "브러시 5분+마사지 10분+낮잠 5분.", "힐링,주말,루틴,이완"),
    ("21-day-cat-massage-challenge", "21일 챌린지", "📅", "21일 고양이 마사지 챌린지 — 습관 만들기", "매일 같은 시간 5분, 체크리스트 포함.", "습관,21일,챌린지,루틴"),
    ("cat-massage-info-hub", "정보 허브", "📚", "고양이 마사지 정보 허브 — 가이드·팁·FAQ 모음", "입문부터 부위별·시즌별 글을 한곳에 연결.", "정보허브,고양이마사지,가이드,SEO"),
    ("purr-massage-science", "골골송·이완", "😻", "골골송과 마사지 — 이완 반응 이해하기", "골골송이 나올 때 터치를 이어가는 법과 멈출 때.", "골골송,이완,반응,과학"),
]


def generic_content(title: str, category: str, extra: str = "") -> str:
    return body(
        f"<p><strong>{title}</strong> — {category} 관점에서 고양이 마사지·이완·웰니스를 연결한 실용 가이드입니다. 20~50대 마사지·힐링 관심 집사를 위해 친근하게 정리했어요.</p>",
        sec(
            "왜 고양이 마사지인가",
            "천천한 터치는 고양이의 긴장을 낮추고, 집사와의 유대감을 키우는 데 도움이 될 수 있습니다.",
            extra,
        ),
        sec(
            "3분 따라하기",
            "<ol><li>고양이가 편한 자세인지 확인</li><li>볼·목 뒤 1분 가볍게 스트로킹</li><li>반응 보며 등·옆구리 2분</li></ol>",
        ),
        tip("매일 비슷한 시간에 하면 고양이가 기대하는 루틴이 됩니다."),
        warn("웰니스 정보이며 수의 진료를 대체하지 않습니다. 이상 증상은 수의사와 상담하세요."),
    )


def build_more_specs():
    for row in MORE_SPECS:
        pid, cat, emoji, title, summary, tags = row
        extra = ""
        if "허브" in title:
            extra = "가이드·팁·FAQ 페이지와 함께 보면 전체 그림이 잡힙니다."
        POST_SPECS.append(
            (pid, cat, emoji, title, summary, tags, lambda t=title, c=cat, e=extra: generic_content(t, c, e))
        )


def make_posts() -> list[dict]:
    build_more_specs()
    assert len(POST_SPECS) == 50, f"expected 50 posts, got {len(POST_SPECS)}"
    categories = [s[1] for s in POST_SPECS]
    assert len(categories) == len(set(categories)), "duplicate categories!"

    start = date(2026, 1, 8)
    posts = []
    for i, spec in enumerate(POST_SPECS):
        pid, cat, emoji, title, summary, tags, content_fn = spec
        tag_list = [t.strip() for t in tags.split(",")]
        posts.append(
            {
                "id": pid,
                "title": title,
                "summary": summary,
                "category": cat,
                "content": content_fn(),
                "tags": tag_list,
                "author": "고양이",
                "date": (start + timedelta(days=i * 3)).isoformat(),
                "emoji": emoji,
                "published": True,
            }
        )
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def main() -> None:
    posts = make_posts()
    OUT.write_text(
        json.dumps({"posts": posts}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(posts)} posts to {OUT}")
    cats = sorted({p["category"] for p in posts})
    print(f"Categories ({len(cats)}): unique OK")


if __name__ == "__main__":
    main()
