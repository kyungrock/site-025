# Appwrite Sites 배포 (Back4app 호스팅 연동용) — site-025
# 사용법: PowerShell에서 이 폴더로 이동 후 .\deploy.ps1

$ErrorActionPreference = "Stop"
$SiteDir = $PSScriptRoot
Set-Location $SiteDir

Write-Host "=== 고양이 (site-025) 정적 사이트 배포 ===" -ForegroundColor Cyan

if (-not (Get-Command appwrite -ErrorAction SilentlyContinue)) {
    Write-Host "Appwrite CLI 설치 중..." -ForegroundColor Yellow
    npm install -g appwrite-cli
}

Write-Host "CLI 버전: $(appwrite -v)" -ForegroundColor Green

$prevErrorAction = $ErrorActionPreference
$ErrorActionPreference = "Continue"
appwrite account get *> $null
$loggedIn = ($LASTEXITCODE -eq 0)
$ErrorActionPreference = $prevErrorAction

if (-not $loggedIn) {
    Write-Host "Appwrite 로그인이 필요합니다." -ForegroundColor Yellow
    appwrite login --endpoint https://fra.cloud.appwrite.io/v1
    if ($LASTEXITCODE -ne 0) { throw "로그인 실패" }
}

$configPath = Join-Path $SiteDir "appwrite.config.json"
$config = Get-Content $configPath -Raw | ConvertFrom-Json

if (-not $config.projectId) {
    Write-Host "appwrite init project 로 프로젝트를 연결하세요." -ForegroundColor Yellow
    appwrite init project
}

Write-Host "사이트 배포 중 (appwrite push sites)..." -ForegroundColor Cyan
appwrite push sites

if ($LASTEXITCODE -eq 0) {
    Write-Host "배포 완료! Console > Sites 에서 URL을 확인하세요." -ForegroundColor Green
    Write-Host "config/site.json 의 deploy_url·domain 을 실제 URL로 갱신 후 publish_blog.py 를 다시 실행하세요." -ForegroundColor Gray
} else {
    exit 1
}
