import { NextPage } from "next";
import QuickCard from "../../components/quickCard";

const Stats: NextPage = () => {
    return(
        <div>
            <div className='container'>
                <div className='title'>Show Stats</div>
                <div className='card-wrapper'>
                    <QuickCard title='Player Stats' link='/stats/player' imgSrc='/player.jpg' />
                    <QuickCard title='Team Stats' link='/stats/team' imgSrc='/team.jpg' />
                    <QuickCard title='Match Stats' link='/stats/match' imgSrc='/tournament.jpg' />
                </div>
            </div>
        </div>
    )
}

export default Stats;