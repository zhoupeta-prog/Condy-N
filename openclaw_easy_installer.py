#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenClaw 懶人包安裝器
一鍵安裝 OpenClaw，完整中文化界面

作者：Condy N. 🐙
GitHub: https://github.com/zhoupeta-prog/Condy-N
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path
from typing import Optional, Tuple

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.prompt import Prompt, Confirm
    from rich.table import Table
    from rich import box
except ImportError:
    print("正在安裝必要的依賴...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich", "-q"])
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.prompt import Prompt, Confirm
    from rich.table import Table
    from rich import box

console = Console()


class OpenClawInstaller:
    """OpenClaw 懶人包安裝器主類別"""
    
    def __init__(self):
        self.system = platform.system()
        self.node_version: Optional[str] = None
        self.npm_version: Optional[str] = None
        self.openclaw_installed = False
        
    def print_banner(self):
        """顯示歡迎橫幅"""
        banner = Text()
        banner.append("🦞 ", style="cyan")
        banner.append("OpenClaw 懶人包安裝器\n", style="bold cyan")
        banner.append("讓安裝變得簡單，讓 AI 觸手可及", style="dim")
        
        console.print(Panel(
            banner,
            border_style="cyan",
            box=box.ROUNDED
        ))
        
    def check_prerequisites(self) -> Tuple[bool, list]:
        """檢查系統環境"""
        issues = []
        
        # 檢查 Node.js
        node_path = shutil.which("node")
        if node_path:
            try:
                result = subprocess.run(
                    ["node", "--version"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                self.node_version = result.stdout.strip()
                # 檢查版本是否 >= 22
                version_num = self.node_version.replace("v", "").split(".")[0]
                if int(version_num) < 22:
                    issues.append(f"Node.js 版本過舊 ({self.node_version})，需要 22+")
            except:
                issues.append("Node.js 檢測失敗")
        else:
            issues.append("未安裝 Node.js")
            
        # 檢查 npm
        npm_path = shutil.which("npm")
        if npm_path:
            try:
                result = subprocess.run(
                    ["npm", "--version"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                self.npm_version = result.stdout.strip()
            except:
                issues.append("npm 檢測失敗")
        else:
            issues.append("未安裝 npm")
            
        # 檢查 curl
        if not shutil.which("curl"):
            issues.append("未安裝 curl（安裝必需）")
            
        return len(issues) == 0, issues
        
    def show_system_info(self):
        """顯示系統資訊"""
        table = Table(title="📊 系統環境檢測", box=box.ROUNDED)
        table.add_column("項目", style="cyan")
        table.add_column("狀態", style="green")
        table.add_column("版本/資訊", style="yellow")
        
        # 作業系統
        table.add_row("作業系統", "✅", f"{self.system} {platform.release()}")
        
        # Node.js
        if self.node_version:
            table.add_row("Node.js", "✅ 已安裝", self.node_version)
        else:
            table.add_row("Node.js", "❌ 未安裝", "將自動安裝")
            
        # npm
        if self.npm_version:
            table.add_row("npm", "✅ 已安裝", self.npm_version)
        else:
            table.add_row("npm", "❌ 未安裝", "將隨 Node 安裝")
            
        # OpenClaw
        openclaw_path = shutil.which("openclaw")
        if openclaw_path:
            self.openclaw_installed = True
            try:
                result = subprocess.run(
                    ["openclaw", "--version"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                version = result.stdout.strip()
                table.add_row("OpenClaw", "✅ 已安裝", version)
            except:
                table.add_row("OpenClaw", "✅ 已安裝", "版本未知")
        else:
            table.add_row("OpenClaw", "⏳ 待安裝", "即將開始")
            
        console.print(table)
        console.print()
        
    def install_node(self) -> bool:
        """安裝 Node.js"""
        console.print("[cyan]📦 正在安裝 Node.js...[/cyan]")
        
        try:
            if self.system == "Darwin":  # macOS
                if shutil.which("brew"):
                    subprocess.run(["brew", "install", "node@22"], check=True)
                else:
                    # 使用 nvm 安裝
                    install_script = """
                    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
                    export NVM_DIR="$HOME/.nvm"
                    [ -s "$NVM_DIR/nvm.sh" ] && \ . "$NVM_DIR/nvm.sh"
                    nvm install 22
                    nvm use 22
                    """
                    subprocess.run(install_script, shell=True, check=True)
                    
            elif self.system == "Linux":
                # 使用 NodeSource
                install_script = """
                curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
                sudo apt-get install -y nodejs
                """
                subprocess.run(install_script, shell=True, check=True)
                
            console.print("[green]✅ Node.js 安裝完成！[/green]")
            return True
            
        except subprocess.CalledProcessError as e:
            console.print(f"[red]❌ Node.js 安裝失敗: {e}[/red]")
            return False
            
    def install_openclaw(self) -> bool:
        """安裝 OpenClaw"""
        console.print("[cyan]🦞 正在安裝 OpenClaw...[/cyan]")
        
        try:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
            ) as progress:
                task = progress.add_task("下載並安裝 OpenClaw...", total=None)
                
                if self.system in ["Darwin", "Linux"]:
                    install_cmd = "curl -fsSL https://openclaw.ai/install.sh | bash"
                else:
                    install_cmd = 'powershell -Command "iwr -useb https://openclaw.ai/install.ps1 | iex"'
                    
                result = subprocess.run(
                    install_cmd,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=120
                )
                
                if result.returncode == 0:
                    progress.update(task, completed=True)
                    console.print("[green]✅ OpenClaw CLI 安裝完成！[/green]")
                    return True
                else:
                    console.print(f"[red]❌ 安裝失敗: {result.stderr}[/red]")
                    return False
                    
        except subprocess.TimeoutExpired:
            console.print("[red]❌ 安裝超時，請檢查網路連線[/red]")
            return False
        except Exception as e:
            console.print(f"[red]❌ 安裝出錯: {e}[/red]")
            return False
            
    def run_onboarding(self) -> bool:
        """運行配置嚮導"""
        console.print()
        console.print(Panel(
            "[bold cyan]⚙️ 現在開始配置 OpenClaw[/bold cyan]\n\n"
            "接下來會引導你完成：\n"
            "• API 金鑰設定（Moonshot/OpenAI 等）\n"
            "• Gateway 服務配置\n"
            "• 聊天頻道連接（選擇性）",
            border_style="blue",
            box=box.ROUNDED
        ))
        
        if Confirm.ask("是否開始配置嚮導？", default=True):
            try:
                # 使用交互式方式運行 onboard
                console.print("[cyan]啟動配置嚮導...[/cyan]")
                subprocess.run(["openclaw", "configure"], check=False)
                return True
            except Exception as e:
                console.print(f"[yellow]⚠️ 配置過程出錯，請手動運行: openclaw configure[/yellow]")
                return False
        return False
        
    def verify_installation(self) -> bool:
        """驗證安裝"""
        console.print()
        console.print("[cyan]🔍 驗證安裝...[/cyan]")
        
        checks = []
        
        # 檢查 openclaw 命令
        if shutil.which("openclaw"):
            checks.append(("OpenClaw CLI", "✅", "green"))
        else:
            checks.append(("OpenClaw CLI", "❌", "red"))
            
        # 檢查 gateway
        try:
            result = subprocess.run(
                ["openclaw", "gateway", "status"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if "running" in result.stdout.lower() or result.returncode == 0:
                checks.append(("Gateway 服務", "✅", "green"))
            else:
                checks.append(("Gateway 服務", "⚠️ 未啟動", "yellow"))
        except:
            checks.append(("Gateway 服務", "⚠️ 未啟動", "yellow"))
            
        # 顯示結果
        table = Table(title="✅ 安裝驗證結果", box=box.ROUNDED)
        table.add_column("組件", style="cyan")
        table.add_column("狀態")
        
        for name, status, color in checks:
            table.add_row(name, f"[{color}]{status}[/{color}]")
            
        console.print(table)
        
        return all(c[1] == "✅" for c in checks if c[0] == "OpenClaw CLI")
        
    def show_next_steps(self):
        """顯示後續步驟"""
        console.print()
        console.print(Panel(
            "[bold green]🎉 安裝完成！[/bold green]\n\n"
            "[bold cyan]常用命令：[/bold cyan]\n"
            "  openclaw dashboard      開啟控制面板（網頁聊天）\n"
            "  openclaw gateway start  啟動 Gateway 服務\n"
            "  openclaw --help         查看所有命令\n\n"
            "[bold cyan]快速開始：[/bold cyan]\n"
            "  1. 運行: openclaw dashboard\n"
            "  2. 瀏覽器會自動打開 http://127.0.0.1:18789/\n"
            "  3. 開始和你的 AI 助手對話！\n\n"
            "[dim]需要連接 Telegram/Discord？運行: openclaw channels telegram setup[/dim]",
            border_style="green",
            box=box.ROUNDED
        ))
        
    def run(self):
        """主運行流程"""
        self.print_banner()
        
        # 檢查環境
        console.print("[cyan]🔍 檢測系統環境...[/cyan]")
        is_ready, issues = self.check_prerequisites()
        self.show_system_info()
        
        if not is_ready:
            console.print("[yellow]⚠️ 發現環境問題，需要修復後才能繼續[/yellow]")
            for issue in issues:
                console.print(f"  • {issue}")
            console.print()
            
            if Confirm.ask("是否自動修復環境？", default=True):
                if not self.node_version:
                    if not self.install_node():
                        console.print("[red]❌ 環境修復失敗，請手動安裝 Node.js 22+[/red]")
                        return
                        
        # 安裝 OpenClaw
        if not self.openclaw_installed:
            if not self.install_openclaw():
                console.print("[red]❌ OpenClaw 安裝失敗[/red]")
                return
        else:
            console.print("[green]✅ OpenClaw 已安裝，跳過安裝步驟[/green]")
            
        # 運行配置
        self.run_onboarding()
        
        # 驗證
        self.verify_installation()
        
        # 顯示後續步驟
        self.show_next_steps()
        
        console.print()
        console.print("[dim]感謝使用 OpenClaw 懶人包安裝器！[/dim]")
        console.print("[dim cyan]👩‍💻 作者：Condy N. 🐙 | 讓技術觸手可及[/dim cyan]")
        console.print("[dim]如果覺得有幫助，歡迎贊助支持持續創作 💜[/dim]")


def main():
    """入口函數"""
    try:
        installer = OpenClawInstaller()
        installer.run()
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️ 安裝已取消[/yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[red]❌ 發生錯誤: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
