import axios from "axios";
import { useRouter } from "next/router";
import { useState } from "react";
import { BACKEND_URL } from "../../utils/constants";

const NewTeam = () => {

    const [name, setName] = useState<string>('');

    const router = useRouter();

    const createTeam = () => {
        axios.post(`${BACKEND_URL}/teams`, {name: name})
            .then((response) => {
                router.replace('/teams')
            })
            .catch((err) => console.log(err));
    }

    return(
        <div className="new-team-page">
            <h1>Create a new team here <span>( Note that players will be taken randomly from a pool of uncapped players )</span></h1>
            <div className="division">
                {/* <div className="divided-block">
                    <button>Generate a team with random name</button>
                </div>
                <div className="divider">
                    OR
                </div> */}
                <div className="divided-block">
                    <input type='text' placeholder="Enter team name" onChange={(event) => setName(event.target.value)}></input>
                    <button onClick={() => createTeam()}>Create team</button>
                </div>
            </div>
        </div>
    )
}

export default NewTeam;