import { useRouter } from "next/router"
import { getTeamFromID } from "../../utils/helpers";

const Team = () => {

    const router = useRouter();
    const team = getTeamFromID(router.query.id);

    return(
        <div className="teams-page">{
            team === null ? (
                <h1>No valid team found</h1>
            )
            : (
                <div className="teams-page-container">
                    <h1>{team.name}</h1>
                    <div className="team-top-bar">
                        <div className="team-highlight">
                            <h2>Captain</h2>
                            <div>{team.captain}</div>
                        </div>
                        <div className="team-highlight">
                            <h2>Wicket Keeper</h2>
                            <div>{team.wicketKeeper}</div>
                        </div>
                        <div className="team-highlight">
                            <h2>Coach</h2>
                            <div>{team.coach}</div>
                        </div>
                    </div>
                </div>
            )
        }</div>
    )
}

export default Team;