import Top100 from './Top100.js';
import Filter from './Filter.js';

import mainStyles from './Main.module.css'

import { Suspense, lazy } from 'react';

function Main(){

    const Filter = lazy(()=> import("./Filter.js"))

    return (
        <div className={mainStyles.mainPage}>
            <Suspense fallback={<div>Loading...</div>}>
            <Top100 />
            <Filter />
            </Suspense>
        </div>
    );
}
export default Main;