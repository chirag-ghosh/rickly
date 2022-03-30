import { useRouter } from "next/router";
import { getPlayerFromID } from "../../utils/helpers";

const Player = () => {

    const router = useRouter();
    const player = getPlayerFromID(router.query.id);

    return(
        <div className="player-page">
            {
                player === null ? (
                    <h1>No valid player found</h1>
                )
                : (
                    <div className="player-page-container">
                        <h1>{player.name}<span> ({player.category})</span></h1>
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
                                <h2>Gender</h2>
                                <div>{player.gender}</div>
                            </div>
                        </div>
                    </div>
                )
            }
        </div>
    )
}

export default Player;