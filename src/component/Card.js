import cardStyles from "./Card.module.css";

import PropTypes from "prop-types";

import { Link } from "react-router-dom";

import StarBorderIcon from "@mui/icons-material/StarBorder";
import { useState, useEffect, useContext, useRef } from "react";
import axios from "axios";

import { connect, useSelector } from "react-redux";
import { Construction } from "@mui/icons-material";
import { getStore, removeStore } from "../redux/getStore.js";

function Card({ id, img, name, dispatchGetStore }) {
  const PROXY = window.location.hostname === 'localhost' ? '' : '/proxy';
  // const URL = `${PROXY}`;

  const URL = "http://localhost:5000";
  // const URL = "https://mojitoto.herokuapp.com"

  // 리덕스 email, store 값 가져오기
  const reduxState = useSelector((state) => state);
  const email = reduxState.email;
  const storeCocktail = reduxState.store;
 
  //onClick 시 db member 의 store 값 가져오기 axios
  const getMemberInfo = async () => {
    //현재 로그인한 회원 정보 get
    const response = await axios.get(`${URL}/login?email_give=${email}`);
    const memberInfo = JSON.parse(response.data.member_info);
    // 즐겨찾기한 칵테일 데이터 추출
    const DBstoreCocktail = memberInfo[0].store;
    // 칵테일 데이터 redux에 저장
    dispatchGetStore(DBstoreCocktail);
  };

  // 렌더링용 useState
  const [render, setRender] = useState(false);
  // 데이터변경 useRef
  const checked = useRef(false);

 


   // 카드의 칵테일 이름과 리덕스 저장된 칵테일 비교 후 렌더
  function If() {
    if (storeCocktail !== null) {
      return storeCocktail.map((res) =>
        res === name ? (setRender(true), (checked.current = true)) : null
      );
    } else {
      return setRender(false), (checked.current = false);
    }
  }
  // redux store 값에 반응하는 useEffect
  useEffect(() => If(), [storeCocktail]);

  //즐겨찾기 별 클릭
  function onClick() {
    //로그인 상태 판별 토큰 가져오기
    const ValToken = window.Kakao.Auth.getAccessToken();
    
    // 비로그인 시에 로그인 유도
    if (ValToken == null) {
      alert("로그인 먼저 해주세요😎");
    } else {
      checked.current = !checked.current;
      //렌더링용 useState 값 변경
      setRender((current) => !current);
      //db에 post
      axiosPost();
    }
  }

  // 좋아요한 칵테일 db 저장하기
  const axiosPost = () => {
    axios
      .post(`${URL}/favourite`, {
        email_give: email,
        name_give: name,
        checked_give: checked.current ? parseInt(1) : parseInt(0),
      })
      .then((res) => {
        // console.log(res);
        alert("통신성공");
      })
      .catch((error) => {
        // console.log(error);
        console.error(error);
      });
      // 회원db get
    setTimeout(() => getMemberInfo(), 500);
  };

  const [cardHover, setCardHover] = useState(0);
  const [starHover, setStarHover] = useState(0);

  return (
    // 임시 render fale 빼기

    <div>
      <div className={cardStyles.card}
        onMouseEnter={() => setCardHover(1)}
        onMouseLeave={() => setCardHover(0)}>

        {render == 1 || starHover == 1 ?
          <img
            className={cardStyles.star_clicked}
            onClick={onClick}
            src="star.png"
            onMouseEnter={() => setStarHover(1)}
            onMouseLeave={() => setStarHover(0)}
          /> : (cardHover == 1 ?
            <img
              onClick={onClick}
              className={cardStyles.star_unclick}
              src="star.png"
              onMouseEnter={() => setStarHover(1)}
              onMouseLeave={() => setStarHover(0)}
            /> : "")
        }

        <Link to={`/desc:${id}`}>
          <div className={cardStyles.imgContainer}>
            <img className={cardStyles.imgCocktail} src={img} />
            <h3 className={cardStyles.cocktailName}>{name}</h3>
          </div>
        </Link>

      </div>
    </div>
  );
}

Card.propTypes = {
  id: PropTypes.string.isRequired,
  img: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
};

function mapDispatchToProps(dispatch) {
  return {
    dispatchGetStore: (array) => dispatch(getStore(array)),
  };
}

export default connect(null, mapDispatchToProps)(Card);