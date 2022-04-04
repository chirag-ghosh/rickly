import { NextPage } from "next";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { useSearchContext } from "../../hooks/useSearchContext";
import { Team } from "../../types";

const Team: NextPage = () => {

    const [teamsList, setTeamsList] = useState<Team[]>([]);

    const {teamList} = useSearchContext();
    const router = useRouter();

    useEffect(() => {
        setTeamsList([...teamList])
    }, [teamList])

    return(
        <div className="teams-page">
            <button className="button" onClick={() => router.push('/team/new')}>Create new Team</button>
            <h1>List of all teams</h1>
            <div className="team-list">
                {
                    teamsList.map((team) => {
                        return(
                            <div onClick={() => router.push(`team/${team.id}`)} className="team">{team.name}</div>
                        )
                    })
                }
            </div>
        </div>
    )
}

export default Team;