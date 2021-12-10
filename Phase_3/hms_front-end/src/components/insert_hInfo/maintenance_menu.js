import React, { useReducer } from "react";
import { Button, TextField, Paper, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import axios from "axios";
import { useNavigate } from 'react-router-dom';
const cardStyles = makeStyles({
  gridContainer: {
    paddingLeft: "20px",
    paddingRight: "20px",
  },
});

function MaterialUIFormSubmit(props) {
  const navigate = useNavigate();
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
      name: " ",
      started_working: "",
      duty: "",
      phone_number: "",
    }
  );

  const handleSubmit = (evt) => {
    evt.preventDefault();
    formInput["queryType"] = "insert-maintenance";
    let data = { formInput };
    
    axios.post('http://127.0.0.1:5000/maintenceAPI_given_h_name', data)
    .then(function (response) {
      console.log(response.data);
      navigate('/all_maintenance')
    })
    .catch(function (error) {
      console.log(error);
    });

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
              defaultValue={""}
              className={classes.textField}
              helperText="Enter maintenance name"
              onChange={handleInput}
            />
            <TextField
              label="Duty"
              id="margin-normal"
              name="duty"
              defaultValue={""}
              className={classes.textField}
              helperText="Enter duty"
              onChange={handleInput}
            />
            <TextField
              label="Started Working"
              id="margin-normal"
              name="started_working"
              defaultValue={""}
              className={classes.textField}
              helperText="Enter founded date"
              onChange={handleInput}
            />
            <TextField
              label="Phone Number"
              id="margin-normal"
              name="phone_number"
              defaultValue={""}
              className={classes.textField}
              helperText="Enter phone number"
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
