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
  const [medicine, setMedicine] = useState([]);
  const [loading, setLoading] = useState(false);
  useEffect(() => getMedicine(), []);
  const getMedicine = () => {
    axios
      .post("http://127.0.0.1:5000/getMedications", {
        queryType: "hospital-med",
        medication_name: localStorage.getItem("medicine_name"),
        hospital_name: localStorage.getItem("hospital_name"),
      })
      .then(function (response) {
        console.log(response.data);
        setMedicine(response.data);
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
      side_effect: "",
      treatment_for: "",
      type: "",
      cost: ""
    }
  );

  const handleSubmit = (evt) => {
    evt.preventDefault();
    formInput["m_id"] = localStorage.getItem("m_id");
    let data = { formInput };

    axios.post('INSERT HERE', data)
      .then(function (response) {
        console.log(response.data);
      })
      .catch(function (error) {
        console.log(error);
      });

    console.log(data);
  };

  function deleteInfo() {
    formInput["m_id"] = localStorage.getItem("m_id");
    let data = { formInput };
    axios.post('INSERT HERE', data)
      .then(function (response) {
        console.log(response.data);
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
                defaultValue={medicine[0]['name']}
                className={classes.textField}
                helperText="Enter medicine name"
                onChange={handleInput}
              />
              <TextField
                label="Side Effect"
                id="margin-normal"
                name="side_effect"
                defaultValue={medicine[0]['side_effect']}
                className={classes.textField}
                helperText="Enter side effect"
                onChange={handleInput}
              />
              <TextField
                label="Treatment For"
                id="margin-normal"
                name="treatment_for"
                defaultValue={medicine[0]['treament_for']}
                className={classes.textField}
                helperText="Enter treatment for"
                onChange={handleInput}
              />
              <TextField
                label="Type"
                id="margin-normal"
                name="type"
                defaultValue={medicine[0]['type']}
                className={classes.textField}
                helperText="Enter type"
                onChange={handleInput}
              />
              <TextField
                label="Cost"
                id="margin-normal"
                name="cost"
                defaultValue={medicine[0]['cost']}
                className={classes.textField}
                helperText="Enter cost"
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