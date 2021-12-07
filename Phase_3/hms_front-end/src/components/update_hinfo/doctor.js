import React, { useReducer } from "react";
import { Button, TextField, Paper, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import { useEffect, useState } from "react";
import axios from "axios";
const cardStyles = makeStyles({
  gridContainer: {
    paddingLeft: "20px",
    paddingRight: "20px",
  },
});

function MaterialUIFormSubmit(props) {
  const [doctor, setDoctor] = useState([]);
  useEffect(() => getDoctor(), []);
  const getDoctor = () => {
    axios
    .post("http://127.0.0.1:5000/getDoctors", {
      queryType: "hospital-doctor",
      doctor_name: localStorage.getItem("hospital_name"),
      hospital_name: localStorage.getItem("doctor_name"),
    })
    .then(function (response) {
     console.log(response.data);
      setDoctor(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });
  };

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
      phone_number: "",
      started_working: "",
      h_id: ""
    }
  );
  const handleSubmit = (evt) => {
    evt.preventDefault();
    console.log(formInput);

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
      <Paper className={classes.root} justifycontent="center">
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
              label="Phone Number"
              id="margin-normal"
              name="Phone Number"
              defaultValue={formInput.phone_number}
              className={classes.textField}
              helperText="Enter phone number"
              onChange={handleInput}
            />
            <TextField
              label="Started Working"
              id="margin-normal"
              name="Started Working"
              defaultValue={formInput.started_working}
              className={classes.textField}
              helperText="Enter started working"
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
            <Button style={{backgroundColor: 'red', color: '#FFFFFF'}}
              onClick={() => {
                console.log("delete button pressed!");
              }}
              variant="contained"
              className={classes.button}
            >
              Delete
            </Button>
          </form>
        </center>
      </Paper>
    </div>
  );
}

export default MaterialUIFormSubmit;
