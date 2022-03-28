import { useState } from "react";
import Select from "react-select";

type Option = {
    value: string,
    label: string
}

const GenderOptions: Option[] = [
    {
        value: 'Male',
        label: 'Male'
    },
    {
        value: 'Female',
        label: 'Female'
    },
    {
        value: 'Others',
        label: 'Others'
    }
]

const PlayOptions: Option[] = [
    {
        value: 'Batter',
        label: 'Batter'
    },
    {
        value: 'Bowler',
        label: 'Bowler'
    },
    {
        value: 'All-rounder',
        label: 'All-rounder'
    }
]

const NewPlayer = () => {

    const [gender, setGender] = useState<Option>(GenderOptions[0]);
    const [category, setCategory] = useState<Option>(PlayOptions[0]);

    return(
        <div className="new-player-page">
            <h1>Create a new player here</h1>
            <div className="division">
                <div className="divided-block">
                    <button>Generate a random player</button>
                </div>
                <div className="divider">
                    OR
                </div>
                <div className="divided-block">
                    <input type='text' placeholder="Enter player name"></input>
                    <input type='number' placeholder="Enter player age"></input>
                    <Select
                        className="input-select" 
                        options={GenderOptions}
                        onChange={(newValue) => setGender(newValue || GenderOptions[0])}
                    />
                    <Select 
                        className="input-select" 
                        options={PlayOptions}
                        onChange={(newValue) => setCategory(newValue || PlayOptions[0])}
                    />
                    <button>Create player</button>
                </div>
            </div>
        </div>
    )
}

export default NewPlayer;