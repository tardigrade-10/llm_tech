import OpenAI from "openai";
import 'dotenv/config';

const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
    baseURL: "https://proxy.llmclient.com/openai/v1",
    defaultHeaders: {
      "x-llmclient-apikey": process.env.LLMCLIENT_API_KEY,
      
    },
});

const chatCompletion = await openai.chat.completions.create({
  messages: [{ role: "user", content: "hi, how are you? My name is yash." }],
  model: "gpt-3.5-turbo",
});

console.log(chatCompletion.choices[0].message.content);