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
  useEffect(() => getRoom(), []);
  const cards = cardStyles();

  function handleChange(event) {
    setSelected(event.target.value);
  }
  const navigate = useNavigate();
  const getRoom = () => {
    axios
      .post("http://127.0.0.1:5000/getRooms", {
        queryType: "room_nurse_not_fill",
        n_id: localStorage.getItem("n_id"),
        h_id: localStorage.getItem("h_id"),
      })
      .then(function (response) {
        console.log(response.data);
        setValues(response.data);
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

    }
  );

  const handleSubmit = (evt) => {
    evt.preventDefault();
    formInput["n_id"] = localStorage.getItem("n_id");
    formInput["r_id"] = selected.r_id;
    formInput["queryType"] = "insert";
    let data = { formInput };
    
    axios.post('http://127.0.0.1:5000/nurse_room_junc', data)
    .then(function (response) {
      console.log(response.data);
      navigate('/nurse_room')
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
      <Paper className={classes.root} justifyontent="center">
        <center>
          <Typography variant="h5" component="h3">
            {props.formName}
          </Typography>
          <Typography component="p">{props.formDescription}</Typography>

          <form onSubmit={handleSubmit}>
            <FormControl>
              <InputLabel htmlFor="choose-room">Room</InputLabel>
              <Select
                value={selected}
                onChange={handleChange}
                inputProps={{
                  room_name: "room",
                  id: "name",
                }}
              >
                {values.map((value, index) => {
                  return (
                    <MenuItem key={index} value={value}>
                      {value.room_number}
                    </MenuItem>
                  );
                })}
              </Select>
            </FormControl>
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