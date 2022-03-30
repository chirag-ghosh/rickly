import type { NextPage } from 'next'
import QuickCard from '../components/quickCard'

const Home: NextPage = () => {
  return (
    <div>
      <div className='container'>
        <div className='title'>Welcome to Rickly Cricket Tournament Management System!</div>
        <div className='card-wrapper'>
          <QuickCard title='Add Player' link='/player/new' imgSrc='/player.jpg' />
          <QuickCard title='Create Team' link='/team/new' imgSrc='/team.jpg' />
          <QuickCard title='Play Tournament' link='/tournament' imgSrc='/tournament.jpg' />
        </div>
      </div>
    </div>
  )
}

export default Home
