import React from "react";
import { SearchProvider } from "../hooks/useSearchContext";
import Sidebar from "./sidebar";
import Topbar from "./topbar";

const Layout: React.FC<{}> = ({children}) => {

    return(
        <SearchProvider>
            <div className='home'>
                <Sidebar />
                <div className='vertical-container'>
                    <Topbar />
                    <div className='main-area'>
                        {children}
                    </div>
                </div>
            </div>
        </SearchProvider>
    )
}

export default Layout;