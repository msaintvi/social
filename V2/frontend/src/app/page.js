'use client';

import { useState, useEffect } from "react";

export default function Home() {
    const [animeList, setAnimeList] = useState([]);
    const [history, setHistory] = useState([]);
    const [historyAnime, setHistoryAnime] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const [animeRes, historyRes, historyAnimeRes] = await Promise.all([
                    fetch("http://127.0.0.1:8000/api/anime/Luffydou/"),
                    fetch("http://127.0.0.1:8000/api/anime/Luffydou/history/"),
                    fetch("http://127.0.0.1:8000/api/anime/Luffydou/history/anime/")
                ]);

                const [animeData, historyData, historyAnimeData] = await Promise.all([
                    animeRes.json(),
                    historyRes.json(),
                    historyAnimeRes.json()
                ]);

                console.log(animeData.data);
                console.log(historyData.data);
                console.log(historyAnimeData.data);

                setAnimeList(animeData.data || []);
                setHistory(historyData.data || []);
                setHistoryAnime(historyAnimeData.data || []);

            } catch (err) {
                console.error("Error fetching anime data:", err);
            } finally {
                setLoading(false);
            }


        
        };

        fetchData();
    }, []);

    if (loading) return <p>Loading...</p>;

    const renderAnimeSection = (title, list) => (
        <div>
            <h2>{title}</h2>
            {list.length > 0 ? (
                <ul>
                    {list.map((anime, index) => (
                        <li key={index}><strong>{anime.title}</strong></li>
                    ))}
                </ul>
            ) : (
                <p>No data available.</p>
            )}
        </div>
    );

    return (
        <div>
            <h1>Anime Dashboard for Luffydou</h1>
            {renderAnimeSection("1. Regular Anime List", animeList)}
            {renderAnimeSection("2. Watch History Entries", history)}
            {renderAnimeSection("3. Full Anime Details from History", historyAnime)}
        </div>
    );
}
