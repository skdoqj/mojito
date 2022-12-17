import {createSlice, createAsyncThunk} from "@reduxjs/toolkit";
import axios from "axios";

const URL = 'http://localhost:5000'

// createAsyncThunk 생성하기
// export const loadEmojis = createAsyncThunk(
//   // action 이름
//   "load/Bucket",
//   // 처리할 비동기 함수
//   async () => {
//     // 서버에서 데이터를 불러옴
//     // const {data: {emojis}} = await axios.get(`${URL}/emojis`)
//     // const emoji = JSON.parse(emojis);
//     const emoji = {
//           "_id" : "63077ce4fd9d28a6a2c8e810",
//           "name" : "miling Face with Smiling Eyes",
//           "value" : "booziness1",
//           "url" : "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/grapes_1f347.png"
//       }
//     console.log(emoji);
//     // action의 payload 리턴
//     return emoji;
//   }
// );


// const getEmojiReducer = createSlice({
//   name: "getEmoji",
//   initialState: [],
//   reducers: {},
//   // extraReducer에 비동기 함수의 pending, fulfilled, rejected를 처리할 내용을 넣어준다!
//   extraReducers: (builder)=> {
//     //pending: 비동기 작업을 시작했을 때
//     builder.addCase(loadEmojis.pending, (state) => {
//       state.loading = 'pending';
//     });
//     //fulfilled: 비동기 작업이 끝났을 때
//     // fullflled 되었을 때, 서버에서 받아온 데이터를 state에 넣어줌!
//     // 첫번째 파라미터는 redux의 state이고 두번째 파라미터는 action
//     builder.addCase(loadEmojis.fulfilled, (state, action) => {
//       state.loading = 'succeeded';
//       state = action.payload;
//     });
//     //rejected: 오류가 났을 때
//     builder.addCase(loadEmojis.rejected, (state) => {
//       state.loading = 'failed';
//     });
//   }

// })

const getEmojiReducer = createSlice({
  name: "getEmoji",
  initialState: [
    {
    "_id" : "63077ce4fd9d28a6a2c8e810",
    "name" : "miling Face with Smiling Eyes",
    "value" : "booziness1",
    "url" : "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/grapes_1f347.png"
}],
  reducers: {
    getEmoji: (state, action) => {
      return (state = action.payload );
    },
    default: (state, action) => {return {...state}}
  }
});


export const { getEmoji } = getEmojiReducer.actions;

export default getEmojiReducer;