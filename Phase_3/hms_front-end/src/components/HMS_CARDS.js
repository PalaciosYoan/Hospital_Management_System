import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import { useEffect, useState } from "react";
import axios from "axios";

const useStyles = makeStyles({
  root: {
    minWidth: 200,
  },
  bullet: {
    display: "inline-block",
    margin: "0 2px",
    transform: "scale(0.8)",
  },
  title: {
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
  },
});

const d = [
  {
    h_id: "ddbb14ca-d099-409a-a635-ed98491843ca",
    address: "1108 ROSS CLARK CIRCLE DOTHAN AL 26301",
    name: "SOUTHEAST ALABAMA MEDICAL CENTER",
  },
  {
    h_id:"ddbb14ca-d099-409a-a635-ed98491843ca",
    address: "702 N MAIN ST OPP AL 36467",
    name: "DEKALB REGIONAL MEDICAL CENTER",
  }
];

function OutlinedCard() {
  const [hospital, setHospital] = useState([]);

  useEffect(() => getHospital(), []);
  const getHospital = () => {
    axios.get("http://127.0.0.1:5000/gethospital").then((response) => {
      //console.log(response);
      const h = response.data;
      console.log(d);
      setHospital(d);
    });
  };
  const classes = useStyles();
  const bull = <span className={classes.bullet}>•</span>;

  function mapCards(hospital, index) {
    return (
      <Card className={classes.root} variant="outlined" key={index}>
        <CardContent>
          <Typography
            className={classes.title}
            color="textSecondary"
            gutterBottom
          ></Typography>
          <Typography variant="h5" component="h2">
            {hospital.name}
          </Typography>
          <Typography className={classes.pos} color="textSecondary">
            adjective
          </Typography>
          <Typography variant="body2" component="p">
            well meaning and kindly.
            <br />
            {'"a benevolent smile"'}
          </Typography>
        </CardContent>
        <CardActions>
          <Button size="small">Learn More</Button>
        </CardActions>
      </Card>
    );
  }
  return hospital.map(mapCards);
}

export default OutlinedCard;
