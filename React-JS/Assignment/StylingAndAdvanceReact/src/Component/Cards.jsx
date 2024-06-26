import React from 'react'
import { data } from "../Data.js"
export default function Cards() {
    const { card } = data;
    return (
        <div className='px-9'>
            <h2 className='text-5xl py-8'>{card.map((item, i) => (item.heading))}</h2>
            <div className='  flex justify-between' >
                {card.map((item, i) => {
                    return (
                        <div className=''>
                            <img className='w-[100%] h-[350px]'src={item.card_img} alt="" />
                            <p className='w-50 font-light'>{item.card_name}</p>
                            <p>{item.card_price}</p>
                        </div>
                    )
                })}
            </div>
        </div>
    )
}
