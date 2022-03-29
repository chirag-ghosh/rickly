import { useState } from "react";

const NewTeam = () => {

    const [name, setName] = useState<string>('');

    return(
        <div className="new-team-page">
            <h1>Create a new team here <span>( Note that players will be taken randomly from a pool of uncapped players )</span></h1>
            <div className="division">
                <div className="divided-block">
                    <button>Generate a team with random name</button>
                </div>
                <div className="divider">
                    OR
                </div>
                <div className="divided-block">
                    <input type='text' placeholder="Enter team name" onChange={(event) => setName(event.target.value)}></input>
                    <button>Create team</button>
                </div>
            </div>
        </div>
    )
}

export default NewTeam;