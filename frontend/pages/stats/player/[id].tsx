import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { useSearchContext } from "../../../hooks/useSearchContext";
import { Player } from "../../../types";
import { getPlayerFromID } from "../../../utils/helpers";

const Player = () => {

    const {playerList} = useSearchContext();
    const router = useRouter();

    const [player, setPlayer] = useState<any>();

    useEffect(() => {

        setPlayer(getPlayerFromID(router.query.id, playerList));
    }, [playerList]);

    return(
        <div className="player-page">
            <h1>{player?.name}</h1>
            <div className="player-stats-highlight-list">
                <div className="player-highlight red">
                    <h2>Team</h2>
                    <div>{player?.team}</div>
                </div>
                <div className="player-highlight green">
                    <h2>Age</h2>
                    <div>{player?.age}</div>
                </div>
            </div>
            <h2>Batter stats</h2>
            <div className="player-stats-highlight-list">
                <div className="player-highlight blue">
                    <h2>Runs Scored</h2>
                    <div>{player?.runcount}</div>
                </div>
                <div className="player-highlight green">
                    <h2>Half Centuries</h2>
                    <div>{player?._50count}</div>
                </div>
                <div className="player-highlight blue">
                    <h2>Centuries</h2>
                    <div>{player?._1Ccount}</div>
                </div>
            </div>
            <h2>Bowler stats</h2>
            <div className="player-stats-highlight-list">
                <div className="player-highlight blue">
                    <h2>Wickets Taken</h2>
                    <div>{player?.wickount}</div>
                </div>
                <div className="player-highlight green">
                    <h2>5-wickets</h2>
                    <div>{player?._5wcount}</div>
                </div>
                <div className="player-highlight blue">
                    <h2>Catches Taken</h2>
                    <div>{player?.catcount}</div>
                </div>
            </div>
        </div>
    )
}

export default Player;