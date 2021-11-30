import React from "react";
import "./styles.css";
import Card from "./components/HMS_CARDS";
import { Grid } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles({
  gridContainer: {
    paddingLeft: "20px",
    paddingRight: "20px",
  },
});

export default function App() {
  const classes = useStyles();

  return (
    <Grid
      container
      spacing={4}
      className={classes.gridContainer}
      justifyContent="center"
    >
      <Card />
    </Grid>
  );
}