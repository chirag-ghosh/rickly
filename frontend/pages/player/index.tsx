import { NextPage } from "next";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { useSearchContext } from "../../hooks/useSearchContext";
import { Player, Team } from "../../types";
import { sampleTeams } from "../../utils/sampleData";

const Player: NextPage = () => {

    const [playersList, setPlayersList] = useState<Player[]>([]);

    const {players} = useSearchContext();
    const router = useRouter();

    useEffect(() => {
        setPlayersList([...players, ...players, ...players, ...players, ...players, ...players, ...players, ...players])
    })

    return(
        <div className="players-page">
            <h1>List of all players</h1>
            <div className="player-list">
                {
                    playersList.map((player) => {
                        return(
                            <div onClick={() => router.push(`player/${player.uuid}`)} className="player">{player.name}</div>
                        )
                    })
                }
            </div>
        </div>
    )
}

export default Player;