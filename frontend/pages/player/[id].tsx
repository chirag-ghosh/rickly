import { useRouter } from "next/router";
import { useSearchContext } from "../../hooks/useSearchContext";
import { getPlayerFromID } from "../../utils/helpers";

const Player = () => {

    const {playerList} = useSearchContext();
    const router = useRouter();
    const player = getPlayerFromID(router.query.id, playerList);

    return(
        <div className="player-page">
            {
                player === null ? (
                    <h1>No valid player found</h1>
                )
                : (
                    <div className="player-page-container">
                        <h1>{player.name}<span> ({player.role})</span></h1>
                        <div className="player-highlight-list">
                            <div className="player-highlight red">
                                <h2>Age</h2>
                                <div>{player.age}</div>
                            </div>
                            <div className="player-highlight green">
                                <h2>Team</h2>
                                <div>{player.team}</div>
                            </div>
                            <div className="player-highlight blue">
                                <h2>Specifics</h2>
                                <div>{player.specifics}</div>
                            </div>
                            <div className="player-highlight green">
                                <h2>Batting Hand</h2>
                                <div>{player.bathandedness}</div>
                            </div>
                            <div className="player-highlight red">
                                <h2>Bowling Hand</h2>
                                <div>{player.ballhandedness}</div>
                            </div>
                        </div>
                    </div>
                )
            }
        </div>
    )
}

export default Player;