import { NextComponentType } from "next";
import { useState } from "react";
import { User, UserX } from "react-feather";
import Search from "./search";

const Topbar: NextComponentType = () => {

    const [authMode, setAuthMode] = useState<'Administrator' | 'Not signed in'>('Not signed in');

    return(
        <div className="topbar">
            <Search />
            <div className={`sign-in-status ${authMode === 'Administrator' ? 'active' : ''}`}>
                <div className="user-icon">{authMode === 'Administrator' ? <User size={20} /> : <UserX size={20} /> }</div>
                <div>{authMode}</div>
            </div>
        </div>
    )
}

export default Topbar;