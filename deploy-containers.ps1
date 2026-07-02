# Back4app Containers 배포 준비 (site-025)
# 1) GitHub 푸시  2) Back4app 대시보드에서 Container 앱 생성

$ErrorActionPreference = "Stop"
$SiteDir = $PSScriptRoot
Set-Location $SiteDir

Write-Host "=== site-025 Back4app Containers 배포 준비 ===" -ForegroundColor Cyan

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "Docker 미설치 — 로컬 빌드 테스트는 건너뜁니다." -ForegroundColor Yellow
} else {
    Write-Host "Docker 이미지 로컬 빌드 테스트..." -ForegroundColor Cyan
    docker build -t site-025 .
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Docker 빌드 성공" -ForegroundColor Green
    } else {
        Write-Host "Docker 빌드 실패 — Dockerfile/nginx.conf 확인" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "다음 단계 (Back4app 웹):" -ForegroundColor Cyan
Write-Host "  1. GitHub에 이 폴더 푸시 (repo 예: site-025)" -ForegroundColor Gray
Write-Host "  2. back4app.com > My Apps > New App > Container as a Service" -ForegroundColor Gray
Write-Host "  3. Import GitHub Repo > site-025 선택" -ForegroundColor Gray
Write-Host "  4. Name: site-025 | Branch: main | Root: / (루트)" -ForegroundColor Gray
Write-Host "  5. Plan: Free > Create App" -ForegroundColor Gray
Write-Host ""
Write-Host "배포 URL 받은 뒤:" -ForegroundColor Cyan
Write-Host "  config/site.json 의 deploy_url, domain 수정" -ForegroundColor Gray
Write-Host "  js/site-config.js 의 baseUrl 수정" -ForegroundColor Gray
Write-Host "  python scripts/publish_blog.py" -ForegroundColor Gray
