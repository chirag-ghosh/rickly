import { NextComponentType } from "next";
import Link from "next/link";
import { BarChart2, Star, User, Users } from "react-feather";

const Sidebar: NextComponentType = () => {
    return(
        <div className="sidebar">
            <Link href='/'>
                <div className="title-bar">
                    <img src="/logo.png" alt="rickly-logo"></img>
                    <div>RICKLY</div>
                </div>
            </Link>
            <div className="option-list">
                <Link href="/team">
                    <div className="option">
                        <Users size={35} />
                        <div> Team</div>
                    </div>
                </Link>
                <Link href="/player">
                    <div className="option">
                        <User size={35} />
                        <div> Players</div>
                    </div>
                </Link>
                <Link href="/stats">
                    <div className="option">
                        <BarChart2 size={35} />
                        <div> Statistics</div>
                    </div>
                </Link>
                <Link href="/tournament">
                    <div className="option">
                        <Star size={35} />
                        <div> Tournament</div>
                    </div>
                </Link>
            </div>
        </div>
    )
}

export default Sidebar;