import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { useSearchContext } from "../../../hooks/useSearchContext";
import { getPlayerFromID } from "../../../utils/helpers";

const Player = () => {

    const {playerList} = useSearchContext();
    const router = useRouter();
    const player = getPlayerFromID(router.query.id, playerList);

    const [matchCount, setMatchCount] = useState<number>();
    const [totalRuns, setTotalRuns] = useState<number>();
    const [totalBalls, setTotalBalls] = useState<number>();
    const [runsGiven, setRunsGiven] = useState<number>();
    const [ballsDelivered, setBallsDelivered] = useState<number>();
    const [wicketsTaken, setWicketsTaken] = useState<number>();

    useEffect(() => {

        setMatchCount(5);
        setTotalRuns(240);
        setTotalBalls(200);

        setRunsGiven(50);
        setBallsDelivered(30);
        setWicketsTaken(1);
    }, []);

    return(
        <div className="player-page">
            <h1>{player?.name}</h1>
            <div className="player-stats-highlight-list">
                <div className="player-highlight red">
                    <h2>Team</h2>
                    <div>{player?.team}</div>
                </div>
                <div className="player-highlight green">
                    <h2>Matches played</h2>
                    <div>{matchCount}</div>
                </div>
            </div>
            <h2>Batter stats</h2>
            <div className="player-stats-highlight-list">
                <div className="player-highlight blue">
                    <h2>Runs Scored</h2>
                    <div>{totalRuns}</div>
                </div>
                <div className="player-highlight green">
                    <h2>Balls played</h2>
                    <div>{totalBalls}</div>
                </div>
                <div className="player-highlight blue">
                    <h2>Average</h2>
                    <div>{matchCount !== undefined && matchCount !== 0 && totalRuns !== undefined ? (totalRuns/matchCount) : '-'}</div>
                </div>
                <div className="player-highlight red">
                    <h2>Strike Rate</h2>
                    <div>{totalBalls !== undefined && totalBalls !== 0 && totalRuns !== undefined ? (totalRuns/totalBalls * 100) : '-'}</div>
                </div>
            </div>
            <h2>Bowler stats</h2>
            <div className="player-stats-highlight-list">
                <div className="player-highlight blue">
                    <h2>Balls delivered</h2>
                    <div>{totalBalls}</div>
                </div>
                <div className="player-highlight green">
                    <h2>Runs given</h2>
                    <div>{totalRuns}</div>
                </div>
                <div className="player-highlight blue">
                    <h2>Wickets Taken</h2>
                    <div>{wicketsTaken}</div>
                </div>
                <div className="player-highlight red">
                    <h2>Economy</h2>
                    <div>{ballsDelivered !== undefined && ballsDelivered !== 0 && runsGiven !== undefined ? (runsGiven/ballsDelivered * 100) : '-'}</div>
                </div>
            </div>
        </div>
    )
}

export default Player;