import { NextPage } from "next";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { useSearchContext } from "../../../hooks/useSearchContext";
import { Player, Team } from "../../../types";

const Player: NextPage = () => {

    const [playersList, setPlayersList] = useState<Player[]>([]);

    const {playerList} = useSearchContext();
    const router = useRouter();

    useEffect(() => {
        setPlayersList([...playerList])
    }, [playerList])

    return(
        <div className="players-page">
            <h1>List of all players</h1>
            <div className="player-list">
                {
                    playersList.map((player) => {
                        return(
                            <div onClick={() => router.push(`/stats/player/${player.id}`)} className="player">{player.name}</div>
                        )
                    })
                }
            </div>
        </div>
    )
}

export default Player;