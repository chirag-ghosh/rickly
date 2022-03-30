import { NextPage } from "next";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { Tournament } from "../../types";
import { sampleTournaments } from "../../utils/sampleData";

const Tournament: NextPage = () => {

    const [newTournamentName, setNewTournamentName] = useState<string>('');
    const [mode, setMode] = useState<('unscheduled' | 'scheduled' | 'completed')>('unscheduled');
    const [tournamentList, setTournamentList] = useState<Tournament[]>([]);

    const router = useRouter();

    useEffect(() => {

        setTournamentList(sampleTournaments.filter((tournament) => {
            if(mode === 'unscheduled')
                return !tournament.scheduled;
            else if(mode === 'scheduled')
                return (tournament.scheduled && !tournament.completed);
            else
                return tournament.completed;

        }));
    }, [mode]);

    return(
        <div className="tournaments-page">
            <h1>Tournaments</h1>
            <div className="new-tournament">
                <h2>Create new Tournament <span>( All teams present will be played )</span></h2>
                <div className="input-bar">
                    <input type='text' placeholder="Enter tournament name" onChange={(event) => setNewTournamentName(event.target.value)}></input>
                    <button>Create tournament</button>
                </div>
            </div>
            <div className="browse-tournaments">
                <h2>Browse tournaments</h2>
                <div className="button-group">
                    <button onClick={() => setMode('unscheduled')} className={`${mode === 'unscheduled' ? 'active' : ''}`}>Unscheduled</button>
                    <button onClick={() => setMode('scheduled')} className={`${mode === 'scheduled' ? 'active' : ''}`}>Scheduled</button>
                    <button onClick={() => setMode('completed')} className={`${mode === 'completed' ? 'active' : ''}`}>Completed</button>
                </div>
                <div className="tournament-list">
                    {
                        tournamentList.map((tournament) => {
                            return(
                                <div onClick={() => router.push(`tournament/${tournament.id}`)}>{tournament.name}</div>
                            )
                        })
                    }
                </div>
            </div>
        </div>
    )
}

export default Tournament;