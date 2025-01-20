import { unWatchProduct, watchProduct } from '@/lib/utils';
import { useState } from 'react';

export interface ItemCardProp {
  _id: string;
  image: string;
  name: string;
  price: string;
  original_price: string;
  link: string;
  ref?: any;
  is_watching?: boolean;
}

const PriceCard = ({ ref, _id,image, name, price, original_price, link, is_watching=false }: ItemCardProp) => {
  const [isWatching, setIsWatching] = useState(is_watching);

  const handleWatchClick = async () => {
    // Logic for adding/removing from watchlist
    setIsWatching(!isWatching);
    if (!isWatching) {
      // Example: Add product to the watchlist (you can store it in localStorage, state, or database)
      const data = await watchProduct(_id)
      if (!data.success) {
        console.error("Failed to watch product:", data.error);
        setIsWatching(false);
      }
    } else  {
      const data = await unWatchProduct(_id)
      if (!data.success) {
        console.error("Failed to unwatch product:", data.error);
        setIsWatching(true);
      }
  };
}

  return (
    <div ref={ref} className="max-w-sm rounded-lg overflow-hidden shadow-lg border border-gray-200 bg-white hover:shadow-2xl transition-shadow duration-300">
      {/* Image Section */}
      <div className="relative">
        <img src={image} alt={name} className="w-full h-48 object-cover" />
        <span className="absolute top-2 right-2 bg-red-600 text-white text-xs px-2 py-1 rounded-full">
          -{Math.round(((+original_price - +price) / +original_price) * 100)}%
        </span>
      </div>
      
      {/* Content Section */}
      <div className="p-4">
        <h2 className="text-lg font-semibold text-gray-800 truncate">{name}</h2>
        <div className="flex items-center justify-between mt-2">
          <span className="text-xl font-bold text-teal-600">${price}</span>
          <span className="text-sm line-through text-gray-400">${original_price}</span>
        </div>
        <a
          href={link}
          target="_blank"
          rel="noopener noreferrer"
          className="block mt-4 bg-teal-600 hover:bg-teal-700 text-white text-center py-2 rounded-lg transition-colors duration-300"
        >
          View Details
        </a>
        <button
          onClick={handleWatchClick}
          className={`mt-2 w-full py-2 rounded-lg transition-colors duration-300 ${isWatching ? 'bg-teal-400' : 'bg-gray-400'} text-white`}
        >
          {isWatching ? 'Watching' : 'Watch'}
        </button>
      </div>
    </div>
  );
};

export default PriceCard;
