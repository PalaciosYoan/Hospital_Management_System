import React, { useReducer } from "react";
import { Button, TextField, Paper, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import axios from "axios";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { FormControl, InputLabel, Select, MenuItem } from "@material-ui/core";

const cardStyles = makeStyles({
  gridContainer: {
    paddingLeft: "20px",
    paddingRight: "20px",
  },
});

function MaterialUIFormSubmit(props) {
  const [values, setValues] = React.useState([]);
  const [selected, setSelected] = useState(" ");

  const [values_2, setValues_2] = React.useState([]);
  const [selected_2, setSelected_2] = useState(" ");

  const [values_3, setValues_3] = React.useState([]);
  const [selected_3, setSelected_3] = useState(" ");

  useEffect(() => getDoctor(), []);
  useEffect(() => getRooms(), []);
  useEffect(() => getMedicine(), []);

  const cards = cardStyles();

  function handleChange(event) {
    setSelected(event.target.value);
  }

  function handleChange_2(event) {
    setSelected_2(event.target.value);
  }

  function handleChange_3(event) {
    setSelected_3(event.target.value);
  }
  const navigate = useNavigate();
  const getDoctor = () => {
    axios
      .post("http://127.0.0.1:5000/getDoctors", {
        queryType: "hospital",
        hospital_name: localStorage.getItem("hospital_name"),
      })
      .then(function (response) {
        console.log(response.data);
        setValues(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  const getRooms = () => {
    axios
      .post("http://127.0.0.1:5000/getRooms", {
        queryType: "room_not_filled",
        hospital_name: localStorage.getItem("hospital_name"),
      })
      .then(function (response) {
        console.log(response.data);
        setValues_2(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  const getMedicine = () => {
    axios
      .post("http://127.0.0.1:5000/getMedications", {
        queryType: "get",
        hospital_name: localStorage.getItem("hospital_name"),
      })
      .then(function (response) {
        console.log(response.data);
        setValues_3(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });
  };

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
    }
  );

  const handleSubmit = (evt) => {
    evt.preventDefault();
    formInput["h_name"] = localStorage.getItem("hospital_name");
    formInput["d_name"] = selected.name;
    formInput["room_number"] = selected_2.room_number;
    formInput["medicine_name"] = selected_3.name;
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
      <Paper className={classes.root} justifyontent="center">
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
              helperText="Enter doctor name"
              onChange={handleInput}
            />
            <TextField
              label="Phone Number"
              id="margin-normal"
              name="phone_number"
              defaultValue={formInput.phone_number}
              className={classes.textField}
              helperText="Enter phone number"
              onChange={handleInput}
            />
            <TextField
              label="Started Working"
              id="margin-normal"
              name="started_working"
              defaultValue={formInput.started_working}
              className={classes.textField}
              helperText="Enter started working date"
              onChange={handleInput}
            />
            <FormControl>
              <InputLabel htmlFor="choose-doctor">Doctor</InputLabel>
              <Select
                value={selected}
                onChange={handleChange}
                inputProps={{
                  doctor_name: "doctor",
                  id: "name",
                }}
              >
                {values.map((value, index) => {
                  return (
                    <MenuItem key={index} value={value}>
                      {value.name}
                    </MenuItem>
                  );
                })}
              </Select>
            </FormControl>
            &nbsp;&nbsp;&nbsp;
            <FormControl>
              <InputLabel htmlFor="choose-doctor">Room</InputLabel>
              <Select
                value={selected_2}
                onChange={handleChange_2}
                inputProps={{
                  room_number: "room",
                  id: "name",
                }}
              >
                {values_2.map((value_2, index_2) => {
                  return (
                    <MenuItem key={index_2} value={value_2}>
                      {value_2.room_number}
                    </MenuItem>
                  );
                })}
              </Select>
            </FormControl>
            &nbsp;&nbsp;&nbsp;
            <FormControl>
              <InputLabel htmlFor="choose-doctor">Medicine</InputLabel>
              <Select
                value={selected_3}
                onChange={handleChange_3}
                inputProps={{
                  medicine: "medicine",
                  id: "name",
                }}
              >
                {values_3.map((value_3, index_3) => {
                  return (
                    <MenuItem key={index_3} value={value_3}>
                      {value_3.name}
                    </MenuItem>
                  );
                })}
              </Select>
            </FormControl>
            &nbsp;&nbsp;&nbsp;
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