'use client'

import { useState, useEffect } from "react";

export default function Home() {
    const [animeList, setAnimeList] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/api/anime/Luffydou/")
        // fetch("http://127.0.0.1:8000/api/anime/Luffydou/animelist")
            .then(res => res.json())
            .then(data => {
                console.log(data); // debug
                setAnimeList(data.data); // adjust depending on real shape
            })
            .catch(err => console.error("Failed to fetch:", err));
    }, []);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/api/anime/Luffydou/history")
        // fetch("http://127.0.0.1:8000/api/anime/Luffydou/animelist")
            .then(res => res.json())
            .then(data => {
                console.log(data); // debug
                setAnimeList(data.data); // adjust depending on real shape
            })
            .catch(err => console.error("Failed to fetch:", err));
    }, []);



    return (
        <div>
            <h1>Anime List</h1>
            <ul>
                {animeList && animeList.length > 0 ? (
                    animeList.map((anime, index) => (
                        <li key={index}>
                            <strong>{anime.title}</strong>
                        </li>
                    ))
                ) : (
                    <p>No anime found or loading...</p>
                )}
            </ul>
        </div>
    );
}
