import axios from "axios";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import Select from "react-select";
import { BACKEND_URL } from "../../utils/constants";

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
        label: 'batter'
    },
    {
        value: 'Bowler',
        label: 'bowler'
    },
    {
        value: 'All-rounder',
        label: 'allrounder'
    },
    {
        value: 'WicketKeeper',
        label: 'wicketkeeper'
    }
]

const NewPlayer = () => {

    const router = useRouter();

    const [name, setName] = useState<string>('');
    const [phone, setPhone] = useState<number>();
    const [category, setCategory] = useState<Option>(PlayOptions[0]);

    const generateRandomPlayer = () => {
        axios.post(`${BACKEND_URL}/players`)
            .then((response) => {
                router.replace('/player')
            })
            .catch(err => console.log(err));
    }

    const generateManualPlayer = () => {
        axios.post(`${BACKEND_URL}/players`, {
            name: name,
            age: phone,
            role: category.value
        })
            .then((response) => {
                router.replace('/player')
            })
            .catch(err => console.log(err));
    }

    return(
        <div className="new-player-page">
            <h1>Create a new player here</h1>
            <div className="division">
                <div className="divided-block">
                    <button onClick={() => generateRandomPlayer()}>Generate a random player</button>
                </div>
                <div className="divider">
                    OR
                </div>
                <div className="divided-block">
                    <input type='text' placeholder="Enter player name" onChange={(event) => setName(event.target.value)}></input>
                    <input type='number' placeholder="Enter player age" onChange={(event) => setPhone(parseInt(event.target.value))}></input>
                    <Select 
                        className="input-select" 
                        options={PlayOptions}
                        onChange={(newValue) => setCategory(newValue || PlayOptions[0])}
                    />
                    <button onClick={() => generateManualPlayer()}>Create player</button>
                </div>
            </div>
        </div>
    )
}

export default NewPlayer;