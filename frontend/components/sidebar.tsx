import { NextComponentType } from "next";
import Link from "next/link";

const Sidebar: NextComponentType = () => {
    return(
        <div className="sidebar">
            <div className="title-bar">
                <img src="/logo.png" alt="rickly-logo"></img>
                <div>RICKLY</div>
            </div>
            <div className="options">
                <Link href="/team">Teams</Link>
                <Link href="/player">Players</Link>
                <Link href="/stats">Statistics</Link>
                <Link href="/tournament">Tournament</Link>
            </div>
        </div>
    )
}

export default Sidebar;