/** Back4app 배포 URL (로컬·다른 호스트는 자동 보정) */
window.SITE_CONFIG = {
  baseUrl: "https://site025-qjhniwbk.b4a.run",
  siteName: "고양이",
  slug: "site-025",
  defaultDescription:
    "고양이 마사지·이완 가이드. 반려묘와 함께하는 힐링·웰니스·셀프케어 실용 정보 허브.",
  locale: "ko_KR",
  keywords: "고양이마사지,마사지,힐링,웰니스,셀프케어",
};

function getSiteBase() {
  const cfg = window.SITE_CONFIG?.baseUrl;
  if (cfg && !location.hostname.includes("localhost") && !location.protocol.startsWith("file")) {
    return cfg.replace(/\/$/, "");
  }
  const path = location.pathname.replace(/\/[^/]*$/, "");
  return (location.origin + path).replace(/\/$/, "") || location.origin;
}

function absoluteUrl(relativePath) {
  const base = getSiteBase();
  const path = String(relativePath || "")
    .replace(/^\//, "")
    .replace(/^https?:\/\//, "");
  if (path.startsWith("http")) return path;
  return `${base}/${path}`;
}
