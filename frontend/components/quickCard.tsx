import { useRouter } from "next/router";
import { QuickCardProps } from "../types";

const QuickCard = (props: QuickCardProps) => {

    const router = useRouter();

    return(
        <div className="quick-card" onClick={() => router.push(props.link)}>
            <img src={props.imgSrc} alt={`${props.title} card`}></img>
            <div className="quick-card-title">{props.title}</div>
        </div>
    )
}

export default QuickCard;