# 批量复制HTML文件到对应目录的脚本
$sourceDir = "../考试平台模拟界面"
$targetBaseDir = "."

# 获取所有HTML文件
$htmlFiles = Get-ChildItem -Path $sourceDir -Filter "*.html"

Write-Host "开始复制HTML文件..." -ForegroundColor Green

foreach ($file in $htmlFiles) {
    # 从文件名中提取目录名（去掉.html扩展名）
    $dirName = $file.BaseName
    
    # 检查目标目录是否存在
    $targetDir = Join-Path $targetBaseDir $dirName
    if (Test-Path $targetDir) {
        # 复制文件到目标目录
        $targetPath = Join-Path $targetDir $file.Name
        Copy-Item $file.FullName $targetPath -Force
        Write-Host "已复制: $($file.Name) -> $targetPath" -ForegroundColor Yellow
    } else {
        Write-Host "警告: 目录 $dirName 不存在，跳过文件 $($file.Name)" -ForegroundColor Red
    }
}

Write-Host "复制完成！" -ForegroundColor Green
Write-Host "总共处理了 $($htmlFiles.Count) 个HTML文件" -ForegroundColor Cyan 