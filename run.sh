#!/bin/bash
# -*- coding: utf-8 -*-

# 一键运行脚本
# 用于轻松启动YouTube视频处理系统

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

# 确保环境配置文件存在
check_env_file() {
    if [[ ! -f ".env" && -f ".env.example" ]]; then
        echo -e "${YELLOW}警告: 未找到.env文件，但存在.env.example${NC}"
        echo -e "${YELLOW}请使用.env.example创建并配置.env文件${NC}"
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
    # 新的目录结构
    dirs=(
        "data/raw"
        "data/processed/temp"
        "data/processed/temp/audio"
        "data/processed/temp/converted_audio"
        "data/processed/temp/youtube"
        "data/processed/transcripts"
        "data/processed/translations"
        "data/outputs/md"
        "data/outputs/srt"
        "data/outputs/txt"
        "data/outputs/summaries"
        "data/archive"
        "logs"
        "reports"
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
    echo "  --summarize     生成内容摘要"
    echo "  --cleanup       清理所有中间文件"
    echo "  --config PATH   指定配置文件路径"
}

# 运行主程序
run_main() {
    echo -e "${BLUE}启动YouTube视频处理系统...${NC}"
    python3 main.py "$@"
    exit_code=$?
    
    if [[ $exit_code -eq 0 ]]; then
        echo -e "${GREEN}处理完成，退出码: $exit_code${NC}"
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