import React, { useReducer } from "react";
import { Button, TextField, Paper, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import { useEffect, useState } from "react";
import axios from "axios";
import { FormControl, InputLabel, Select, MenuItem } from "@material-ui/core";
import { useNavigate } from 'react-router-dom';
const cardStyles = makeStyles({
  gridContainer: {
    paddingLeft: "20px",
    paddingRight: "20px",
  },
});

function MaterialUIFormSubmit(props) {
  const navigate = useNavigate();
  const [nurse, setNurse] = useState([]);
  const [loading, setLoading] = useState(false);
  const [values, setValues] = React.useState([]);
  const [selected, setSelected] = useState(" ");

  useEffect(() => getNurse(), []);

  function handleChange(event) {
    setSelected(event.target.value);
  }


  const getNurse = () => {
    axios
      .post("http://127.0.0.1:5000/getNurses", {
        queryType: "nurse-hospital",
        nurse_name: localStorage.getItem("nurse_name"),
        hospital_name: localStorage.getItem("hospital_name"),
      })
      .then(function (response) {
        console.log(response.data);
        setNurse(response.data);
        setLoading(true);
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
      started_working: "",
    }
  );
  const handleSubmit = (evt) => {
    evt.preventDefault();
    formInput["n_id"] = localStorage.getItem("n_id");
    formInput["h_id"] = localStorage.getItem("h_id");
    let data = { formInput };
    axios.put('http://127.0.0.1:5000/getNurses', data)
      .then(function (response) {
        console.log(response.data);
        navigate('/nurse')
      })
      .catch(function (error) {
        console.log(error);
      });

    console.log(data);
  };

  function deleteInfo() {
    formInput["n_id"] = localStorage.getItem("n_id");
    formInput["queryType"] = "delete";
    
    let data = { formInput };
    axios.post('http://127.0.0.1:5000/getNurses', data)
      .then(function (response) {
        console.log(response.data);
        navigate('/nurse')
      })
      .catch(function (error) {
        console.log(error);
      });
    console.log(data);
  }


  const handleInput = (evt) => {

    const name = evt.target.name;
    const newValue = evt.target.value;
    setFormInput({ [name]: newValue });
  };

  const classes = useStyles();

  function renderItems() {    
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
                defaultValue={nurse[0]['name']}
                className={classes.textField}
                helperText="Enter nurse name"
                onChange={handleInput}
              />
              <TextField
                label="Started Working"
                id="margin-normal"
                name="started_working"
                defaultValue={nurse[0]['started_working']}
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
              <Button
                style={{ backgroundColor: "red", color: "#FFFFFF" }}
                onClick={() => {
                  deleteInfo();
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

  return loading ? <div>{renderItems()}</div> : <div>loading...</div>;
}

export default MaterialUIFormSubmit;