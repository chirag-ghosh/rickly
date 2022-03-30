import { NextPage } from "next";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { useSearchContext } from "../../../hooks/useSearchContext";
import { Team } from "../../../types";
import { sampleTeams } from "../../../utils/sampleData";

const Team: NextPage = () => {

    const [teamsList, setTeamsList] = useState<Team[]>([]);

    const {teams} = useSearchContext();
    const router = useRouter();

    useEffect(() => {
        setTeamsList([...teams, ...teams, ...teams, ...teams, ...teams, ...teams, ...teams, ...teams])
    })

    return(
        <div className="teams-page">
            <h1>List of all teams</h1>
            <div className="team-list">
                {
                    teamsList.map((team) => {
                        return(
                            <div onClick={() => router.push(`/stats/team/${team.uuid}`)} className="team">{team.name}</div>
                        )
                    })
                }
            </div>
        </div>
    )
}

export default Team;