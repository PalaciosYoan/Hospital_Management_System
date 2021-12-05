import React, { useReducer } from "react";
import { Button, TextField, Paper, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";

const cardStyles = makeStyles({
  gridContainer: {
    paddingLeft: "20px",
    paddingRight: "20px",
  },
});

function MaterialUIFormSubmit(props) {
  const cards = cardStyles();
  const useStyles = makeStyles((theme) => ({
    button: {
      margin: theme.spacing(1),
    },
    root: {
      padding: theme.spacing(3, 2),
    },
    container: {
      display: "flex",
      flexWrap: "wrap",
    },
    textField: {
      marginLeft: theme.spacing(1),
      marginRight: theme.spacing(1),
      width: 400,
    },
  }));

  const [formInput, setFormInput] = useReducer(
    (state, newState) => ({ ...state, ...newState }),
    {
      name: "",
      address: "",
    }
  );

  const handleSubmit = (evt) => {
    evt.preventDefault();

    let data = { formInput };
    console.log(data);
  };

  const handleInput = (evt) => {
    const name = evt.target.name;
    const newValue = evt.target.value;
    setFormInput({ [name]: newValue });
  };

  const classes = useStyles();

  return (
    <div>
      <div>
        <center>
          <Card className={cards.root} variant="outlined">
            <CardContent>
              <Typography
                className="Hospital"
                color="textSecondary"
                gutterBottom
              ></Typography>
              <Typography variant="h5" component="h2">
                {localStorage.getItem("hospital_name")}
              </Typography>
              <Typography variant="body2" component="p">
                {localStorage.getItem("hospital_address")}
              </Typography>
            </CardContent>
          </Card>
        </center>
        &nbsp;
      </div>
      <Paper className={classes.root} justifyContent="center">
        <center>
          <Typography variant="h5" component="h3">
            {props.formName}
          </Typography>
          <Typography component="p">{props.formDescription}</Typography>

          <form onSubmit={handleSubmit}>
            <TextField
              label="Name"
              id="margin-normal"
              name="name"
              defaultValue={formInput.name}
              className={classes.textField}
              helperText="Enter hospital name"
              onChange={handleInput}
            />
            <TextField
              label="Address"
              id="margin-normal"
              name="address"
              defaultValue={formInput.address}
              className={classes.textField}
              helperText="Enter hospital address"
              onChange={handleInput}
            />
            <Button
              type="submit"
              variant="contained"
              color="primary"
              className={classes.button}
            >
              Submit
            </Button>
          </form>
        </center>
      </Paper>
    </div>
  );
}

export default MaterialUIFormSubmit;
