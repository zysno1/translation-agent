#!/bin/bash
# -*- coding: utf-8 -*-

# 一键运行脚本
# 用于轻松启动YouTube视频处理系统

# 系统版本
SYSTEM_VERSION="v2.0.0"

# 颜色配置
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # 无颜色

# 显示横幅
echo -e "${BLUE}================================${NC}"
echo -e "${GREEN}  YouTube视频处理系统启动脚本  ${NC}"
echo -e "${BLUE}================================${NC}"
echo -e "${GREEN}         版本: ${SYSTEM_VERSION}${NC}"
echo ""

# 验证Python环境
check_python() {
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}错误: 未找到Python3${NC}"
        echo "请安装Python 3.8或更高版本"
        exit 1
    fi
    
    # 检查版本
    python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    echo -e "${BLUE}检测到Python版本: ${python_version}${NC}"
    
    if [[ $(echo "$python_version < 3.8" | bc) -eq 1 ]]; then
        echo -e "${YELLOW}警告: 建议使用Python 3.8或更高版本${NC}"
    fi
}

# 激活虚拟环境
activate_venv() {
    # 检查是否在venv中
    if [[ -z "${VIRTUAL_ENV}" ]]; then
        echo -e "${BLUE}正在激活虚拟环境...${NC}"
        
        # 检查几种常见的虚拟环境路径
        if [[ -f ".venv/bin/activate" ]]; then
            source .venv/bin/activate
            echo -e "${GREEN}虚拟环境已激活: .venv${NC}"
        elif [[ -f "venv/bin/activate" ]]; then
            source venv/bin/activate
            echo -e "${GREEN}虚拟环境已激活: venv${NC}"
        elif [[ -f "ENV/bin/activate" ]]; then
            source ENV/bin/activate
            echo -e "${GREEN}虚拟环境已激活: ENV${NC}"
        else
            echo -e "${YELLOW}警告: 未找到虚拟环境，将使用系统Python${NC}"
        fi
    else
        echo -e "${GREEN}已在虚拟环境中: ${VIRTUAL_ENV}${NC}"
    fi
}

# 确保依赖已安装
check_dependencies() {
    echo -e "${BLUE}检查依赖...${NC}"
    if [[ -f "requirements.txt" ]]; then
        if [[ "$1" == "--install" ]]; then
            echo -e "${BLUE}安装依赖...${NC}"
            pip install -r requirements.txt
            echo -e "${GREEN}依赖已安装${NC}"
        else
            echo -e "${BLUE}提示: 使用 --install 参数安装依赖${NC}"
        fi
    else
        echo -e "${YELLOW}警告: 未找到requirements.txt文件${NC}"
    fi
}

# 确保环境配置文件存在并加载
check_env_file() {
    if [[ -f ".env" ]]; then
        echo -e "${BLUE}加载环境变量文件: .env${NC}"
        source .env
        echo -e "${GREEN}环境变量已加载${NC}"
    elif [[ -f ".env.example" ]]; then
        echo -e "${YELLOW}警告: 未找到.env文件，但存在.env.example${NC}"
        echo -e "${YELLOW}请使用.env.example创建并配置.env文件${NC}"
    else
        echo -e "${YELLOW}警告: 未找到.env文件${NC}"
    fi
}

# 确保配置文件存在
check_config_file() {
    if [[ ! -f "config.yaml" ]]; then
        echo -e "${RED}错误: 未找到config.yaml配置文件${NC}"
        exit 1
    else
        echo -e "${GREEN}配置文件已找到: config.yaml${NC}"
    fi
}

# 确保目录结构正确
check_directories() {
    # 最新目录结构
    dirs=(
        "data/raw"
        "data/processed"
        "data/transcripts"
        "data/translations"
        "data/summaries"
        "temp"
        "temp/audio"
        "temp/converted_audio"
        "temp/video"
        "temp/downloads"
        "reports"
        "logs"
    )
    
    for dir in "${dirs[@]}"; do
        if [[ ! -d "$dir" ]]; then
            echo -e "${BLUE}创建目录: $dir${NC}"
            mkdir -p "$dir"
        fi
    done
    echo -e "${GREEN}目录结构已检查并创建${NC}"
}

# 显示可用示例命令
show_examples() {
    echo -e "${BLUE}可用示例命令:${NC}"
    echo -e "${GREEN}1. 处理YouTube视频:${NC}"
    echo "   ./run.sh --url https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    echo ""
    echo -e "${GREEN}2. 处理本地视频文件:${NC}"
    echo "   ./run.sh --file ./path/to/video.mp4"
    echo ""
    echo -e "${GREEN}3. 批量处理:${NC}"
    echo "   ./run.sh --batch ./path/to/urls.txt"
    echo ""
    echo -e "${GREEN}4. 自定义模板和摘要:${NC}"
    echo "   ./run.sh --url https://www.youtube.com/watch?v=dQw4w9WgXcQ --template academic --summarize"
}

# 显示性能统计
show_stats() {
    echo -e "${BLUE}查找最新的处理报告...${NC}"
    
    # 查找最新的报告文件
    latest_report=$(find ./reports -type f -name "*.md" -print0 | xargs -0 ls -t | head -n 1)
    
    if [[ -z "$latest_report" ]]; then
        echo -e "${YELLOW}未找到任何报告文件${NC}"
        return 1
    fi
    
    echo -e "${GREEN}找到最新报告: ${latest_report}${NC}"
    echo ""
    echo -e "${BLUE}处理统计信息:${NC}"
    
    # 提取并显示处理统计信息
    stats=$(grep -A 10 "## 处理统计" "$latest_report")
    
    if [[ -z "$stats" ]]; then
        echo -e "${YELLOW}未在报告中找到处理统计信息${NC}"
        return 1
    fi
    
    # 提取关键信息
    audio_extraction=$(echo "$stats" | grep "音频提取时间" | sed 's/.*音频提取时间: //')
    transcription=$(echo "$stats" | grep "转写时间" | sed 's/.*转写时间: //')
    translation=$(echo "$stats" | grep "翻译时间" | sed 's/.*翻译时间: //')
    
    # 显示信息
    echo -e "${GREEN}音频提取耗时: ${audio_extraction}${NC}"
    echo -e "${GREEN}转写耗时: ${transcription}${NC}"
    echo -e "${GREEN}翻译耗时: ${translation}${NC}"
    
    echo ""
    echo -e "${BLUE}要查看完整报告，请运行:${NC}"
    echo "open \"$latest_report\""
    
    return 0
}

# 显示帮助信息
show_help() {
    echo -e "${BLUE}用法:${NC}"
    echo "  ./run.sh [选项]"
    echo ""
    echo -e "${BLUE}选项:${NC}"
    echo "  --help          显示此帮助信息"
    echo "  --examples      显示示例命令"
    echo "  --install       安装所需依赖"
    echo "  --verbose       显示详细日志"
    echo "  --url URL       处理YouTube视频URL"
    echo "  --file PATH     处理本地视频文件"
    echo "  --batch PATH    批量处理队列文件"
    echo "  --template TYPE 报告模板 (default, academic, business)"
    echo "  --summarize     生成内容摘要 (已废弃：现在摘要生成是默认行为)"
    echo "  --cleanup       清理所有中间文件"
    echo "  --config PATH   指定配置文件路径"
    echo "  --version       显示当前系统版本"
    echo "  --stats         显示最近处理的性能统计"
    echo ""
    echo -e "${BLUE}特性:${NC}"
    echo "  * 精确时间追踪 - 系统会记录每个处理阶段的耗时"
    echo "  * 自动生成报告 - 处理完成后生成详细的Markdown报告"
    echo "  * 统一OSS转录 - 使用阿里云OSS进行音频转录"
    echo "  * 并行翻译支持 - 长视频启用并行翻译加速处理"
}

# 运行主程序
run_main() {
    echo -e "${BLUE}启动YouTube视频处理系统...${NC}"
    # 记录开始时间
    start_time=$(date +%s)
    
    # 确保环境变量传递给Python进程
    if [[ -f ".env" ]]; then
        # 使用 export 导出环境变量，确保子进程可以访问
        set -a  # 自动导出所有变量
        source .env
        set +a  # 关闭自动导出
    fi
    
    # 运行主程序
    python3 main.py "$@"
    exit_code=$?
    
    # 记录结束时间
    end_time=$(date +%s)
    total_time=$((end_time - start_time))
    
    # 格式化时间显示
    format_time() {
        local sec=$1
        local min=0
        local hr=0
        
        if [ $sec -ge 60 ]; then
            min=$((sec / 60))
            sec=$((sec % 60))
        fi
        
        if [ $min -ge 60 ]; then
            hr=$((min / 60))
            min=$((min % 60))
        fi
        
        if [ $hr -gt 0 ]; then
            echo "${hr}小时${min}分${sec}秒"
        elif [ $min -gt 0 ]; then
            echo "${min}分${sec}秒"
        else
            echo "${sec}秒"
        fi
    }
    
    if [[ $exit_code -eq 0 ]]; then
        echo -e "${GREEN}处理完成，退出码: $exit_code${NC}"
        echo -e "${GREEN}总处理时间: $(format_time $total_time)${NC}"
        echo ""
        echo -e "${BLUE}注意:${NC} 详细的处理时间统计可在生成的报告中查看"
        echo -e "      包括音频提取、转写和翻译各阶段的耗时"
    else
        echo -e "${RED}处理失败，退出码: $exit_code${NC}"
    fi
    
    return $exit_code
}

# 主函数
main() {
    # 检查是否请求帮助
    if [[ "$1" == "--help" ]]; then
        show_help
        exit 0
    fi
    
    # 检查是否请求示例
    if [[ "$1" == "--examples" ]]; then
        show_examples
        exit 0
    fi
    
    # 检查是否请求显示版本
    if [[ "$1" == "--version" ]]; then
        echo -e "${GREEN}YouTube视频处理系统 ${SYSTEM_VERSION}${NC}"
        exit 0
    fi
    
    # 检查是否请求显示统计
    if [[ "$1" == "--stats" ]]; then
        show_stats
        exit $?
    fi
    
    # 初始化环境
    check_python
    activate_venv
    
    # 检查是否请求安装依赖
    if [[ "$1" == "--install" ]]; then
        check_dependencies "--install"
        shift # 移除参数
    else
        check_dependencies
    fi
    
    check_env_file
    check_config_file
    check_directories
    
    # 如果没有参数，显示帮助
    if [[ $# -eq 0 ]]; then
        echo -e "${YELLOW}未提供命令行参数，显示帮助信息${NC}"
        echo ""
        show_help
        echo ""
        echo -e "${YELLOW}显示一些示例命令${NC}"
        echo ""
        show_examples
        exit 1
    fi
    
    # 运行主程序
    run_main "$@"
    exit $?
}

# 执行主函数
main "$@"