import express, {Application, Request, Response} from "express";
import morgan from "morgan";

import dotenv from 'dotenv';
import {Signale} from "signale";
import proxy from "express-http-proxy";

const app:Application = express();
const signale = new Signale();

dotenv.config();

app.use(morgan('dev'));
const PORT = process.env.PORT || 3000;
const GATEWAY = process.env.SERVICE_NAME;


app.use('/api/v1/orders',proxy('http://127.0.0.1:3001'));
app.use('/api/v1/products',proxy('http://127.0.0.1:3002'));


app.listen(PORT, () => {
    signale.success(`Servicio ${GATEWAY} corriendo en http://localhost:${PORT}`);
});
